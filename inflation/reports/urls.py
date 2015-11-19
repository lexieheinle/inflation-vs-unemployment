from django.conf.urls import url
from django.views.generic import ListView
from django.views.generic.dates import *
from . import views
from . import models

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<year>\d{4})/(?P<month>\d{2})/$',
        MonthArchiveView.as_view(
            model=Inflation,
            date_field='date',
        )
        ),
]