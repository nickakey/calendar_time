from django.urls import path, include
from rest_framework import routers
from .views import EventViewSet, authorize, oauth2callback, a_view

router = routers.DefaultRouter()

router.register(r'events', EventViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('a_view/authorize/', authorize, name='authorize'),
    path('oauth2callback', oauth2callback, name='oauth2callback'),
    path('a_view/', a_view, name='a_view'),
]
