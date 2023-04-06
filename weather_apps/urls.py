"""Defines URL patterns for weather_app"""

from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # Home page
    re_path('^$', views.index, name='index'),
]