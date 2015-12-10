from django.conf.urls import url
from . import views
from .models import Inflation, Unemployment, Interest
from inflation import settings

urlpatterns = [
  url(r'^inflation$', views.inflation_overview, name='inflationOver'),  
  url(r'^unemployment$', views.unemployment_overview, name='unemploymentOver'),
  url(r'^interest$', views.interest_overview, name="interestOver"),
  url(r'^sources$', views.source, name='source'),
  url(r'^decade/(?P<decade_num>[0-9]{4})/$', views.time_spans, name='decade_num'),
]


  

