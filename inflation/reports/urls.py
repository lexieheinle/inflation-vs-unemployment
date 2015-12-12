from django.conf.urls import url
from . import views
from .models import Inflation, Unemployment, Interest
from inflation import settings

urlpatterns = [
  url(r'^inflation$', views.Inflation_overview.as_view(), name='inflationOver'),  
  url(r'^unemployment$', views.Unemployment_overview.as_view(), name='unemploymentOver'),
  url(r'^interest$', views.Interest_overview.as_view(), name="interestOver"),
  url(r'^sources$', views.Source.as_view(), name='source'),
  url(r'^decade/1970/$', views.Time_spans1970.as_view(), name='1970s'),
  url(r'^decade/1980/$', views.Time_spans1980.as_view(), name='1980s'),
  url(r'^decade/1990/$', views.Time_spans1990.as_view(), name='1990s'),
  url(r'^decade/2000/$', views.Time_spans2000.as_view(), name='2000s'),
  url(r'^decade/2010/$', views.Time_spans2010.as_view(), name='2010s'),
]


  

