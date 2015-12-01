from django.conf.urls import url
from django.views.generic import ListView
from django.views.generic.dates import *
from . import views
from .models import Inflation, Unemployment, Interest

urlpatterns = [
    url(r'^$', views.index, name='index'),
  url(r'^inflation/([0-9]{4})/([0-9]{2})/$', views.inflation, name='inflation'),
  url(r'^unemployment/([0-9]{4})/([0-9]{2})/$', views.unemployment, name='unemployment'),
  url(r'^interest/([0-9]{4})/([0-9]{2})/$', views.interest, name='interest'),
]