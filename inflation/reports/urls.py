from django.conf.urls import url
from . import views
from .models import Inflation, Unemployment, Interest
from inflation import settings

urlpatterns = [
  url(r'^inflation$', views.InflationOverview.as_view(), name='inflationOver'),  
  url(r'^unemployment$', views.UnemploymentOverview.as_view(), name='unemploymentOver'),
  url(r'^interest$', views.InterestOverview.as_view(), name="interestOver"),
  url(r'^sources$', views.Source.as_view(), name='source'),
  url(r'^decade/1970/$', views.TimeSpans1970.as_view(), name='1970s'),
  url(r'^decade/1980/$', views.TimeSpans1980.as_view(), name='1980s'),
  url(r'^decade/1990/$', views.TimeSpans1990.as_view(), name='1990s'),
  url(r'^decade/2000/$', views.TimeSpans2000.as_view(), name='2000s'),
  url(r'^decade/2010/$', views.TimeSpans2010.as_view(), name='2010s'),
]


  

