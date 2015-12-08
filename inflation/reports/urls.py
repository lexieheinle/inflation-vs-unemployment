from django.conf.urls import url
from django.views.generic import ListView
from django.views.generic.dates import *
from . import views
from .models import Inflation, Unemployment, Interest
from inflation import settings

urlpatterns = [
  url(r'^inflation/([0-9]{4})/([0-9]{2})/$', views.inflation, name='inflation'),
  url(r'^unemployment/([0-9]{4})/([0-9]{2})/$', views.unemployment, name='unemployment'),
  url(r'^interest/([0-9]{4})/([0-9]{2})/$', views.interest, name='interest'),
  url(r'^inflation$', views.inflationOverview, name='inflationOver'),  
  url(r'^unemployment$', views.unemploymentOverview, name='unemploymentOver'),
  url(r'^interest$', views.interestOverview, name="interestOver"),
  url(r'^sources$', views.source, name='source'),
  """url(r'^decade/[0-9]{4}/$', views.decade, name='decade'),"""
] 