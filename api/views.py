from __future__ import print_function
from rest_framework.decorators import api_view
from rest_framework import viewsets
from google.oauth2.credentials import Credentials
from django.urls import reverse
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os.path
import pickle
import datetime
from .models import EventModel
from .serializers import EventSerializer
from rest_framework.response import Response
SCOPES = ['https://www.googleapis.com/auth/calendar']


class EventViewSet(viewsets.ModelViewSet):

    queryset = EventModel.objects.all()
    serializer_class = EventSerializer


@api_view()
def a_view(request):
    if 'credentials' not in request.session:
        request.session['endurl'] = _build_full_view_url(request, 'a_view')
        return HttpResponseRedirect('authorize')

    return Response({"message": "Hello, world!"})


def oauth2callback(request):
    """Authorization callback code, called during oauth callback."""
    state = request.session['state']
    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json", SCOPES, state=state)
    flow.redirect_uri = _build_full_view_url(request, 'oauth2callback')
    authorization_response = request.build_absolute_uri()
    flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials
    request.session['credentials'] = _credentials_to_dict(credentials)
    print("This is the request session ... ", request.session)
    return HttpResponseRedirect(request.session['endurl'])


def authorize(request):
    """Authorizes user's google account so that our code can edit their calendar."""
    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json", SCOPES)
    flow.redirect_uri = _build_full_view_url(request, 'oauth2callback')
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true',
        approval_prompt='force',
    )
    request.session['state'] = state
    return HttpResponseRedirect(authorization_url)


def _build_full_view_url(request, view):
    """Returns the full url route to the view provided."""
    return 'http://' + request.environ['HTTP_HOST'] + reverse(view)


def _credentials_to_dict(credentials):
    """Helper function that adds sign-in credentials to dictionary."""
    return {'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes}
