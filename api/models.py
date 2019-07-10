from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from django.db import models

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

print("oh yeah brother")


class EventModel(models.Model):
    title = models.TextField(max_length=100, default="event")
    count = models.IntegerField(default=0)
    total_minutes = models.IntegerField(default=0)
    category = models.TextField(max_length=100, default="undefined")
