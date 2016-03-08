"""Locations URL configuration"""
from django.conf.urls import url

from .views import HomeView

app_name = 'locations'
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
]
