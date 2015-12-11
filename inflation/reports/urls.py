from django.conf.urls import url
from . import views
from .models import Inflation, Unemployment, Interest
from inflation import settings

urlpatterns = [
  url(r'^inflation$', views.Inflation_overview.as_view(), name='inflationOver'),  
  url(r'^unemployment$', views.Unemployment_overview.as_view(), name='unemploymentOver'),
  url(r'^interest$', views.Interest_overview.as_view(), name="interestOver"),
  url(r'^sources$', views.Source.as_view(), name='source'),
  url(r'^decade/(?P<decade_num>[0-9]{4})/$', views.Time_spans.as_view(), name='decade_num'),
]


  

