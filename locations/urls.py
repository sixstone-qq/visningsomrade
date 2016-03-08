"""Locations URL configuration"""
from django.conf.urls import include, url
from rest_framework import routers


from .views import HomeView, LocationViewSet


# REST framework routing (CRUD on location)
router = routers.DefaultRouter()
router.register(r'locations', LocationViewSet)


app_name = 'locations'
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/', include(router.urls)),
]
