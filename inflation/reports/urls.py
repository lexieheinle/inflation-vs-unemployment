from django.conf.urls import url
from . import views
from .models import Inflation, Unemployment, Interest
from inflation import settings

urlpatterns = [
  url(r'^inflation$', views.inflationOverview, name='inflationOver'),  
  url(r'^unemployment$', views.unemploymentOverview, name='unemploymentOver'),
  url(r'^interest$', views.interestOverview, name="interestOver"),
  url(r'^sources$', views.source, name='source'),
  url(r'^decade/(?P<decade_num>[0-9]{4})/$', views.timeSpans, name='decade_num'),
]


  

