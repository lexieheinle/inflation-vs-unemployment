from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from reports.models import Inflation, Unemployment, Interest
from bakery.views import BuildableDetailView, BuildableListView, BuildableTemplateView

import json
import datetime

# Create your views here.
class Index(BuildableTemplateView):
    stat = 'Index'
    queryset = {'name': stat}
    template_name = 'main.html'
    
class Source(BuildableTemplateView):
    stat = 'Source'
    queryset = {'name': stat}
    template_name = 'source.html'
    
class Unemployment_overview(BuildableListView):
    template_name = "stat.html"
    queryset = []
    def get_context_data(self):
        my_list = []
        for object in Unemployment.objects.all().values():
            little_dict = {}
            little_dict['date'] = str(object['date'])
            little_dict['rate'] = object['rate']
            my_list.append(little_dict)
        json_data = json.dumps(my_list)
        context = super(Unemployment_overview, self).get_context_data()
        context['name'] = 'Unemployment'
        context['json_data'] = json_data
        return context
class Interest_overview(BuildableListView):
    template_name = "stat.html"
    queryset = []
    def get_context_data(self):
        my_list = []
        for object in Interest.objects.all().values():
            little_dict = {}
            little_dict['date'] = str(object['date'])
            little_dict['rate'] = object['rate']
            my_list.append(little_dict)
        json_data = json.dumps(my_list)
        context = super(Interest_overview, self).get_context_data()
        context['name'] = 'Interest'
        context['json_data'] = json_data
        return context
class Inflation_overview(BuildableListView):
    template_name = "stat.html"
    queryset = []
    def get_context_data(self):
        my_list = []
        for object in Inflation.objects.all().values():
            little_dict = {}
            little_dict['date'] = str(object['date'])
            little_dict['rate'] = object['rate']
            my_list.append(little_dict)
        json_data = json.dumps(my_list)
        context = super(Inflation_overview, self).get_context_data()
        context['name'] = 'Inflation'
        context['json_data'] = json_data
        return context
class Time_spans(BuildableListView):
    template_name = "time.html"
    queryset = []
    def get_context_data(self, **kwargs):
        decade_num = self.kwargs['decade_num']
        decade_num = int(decade_num)
        stat = "{0}s".format(decade_num)
        start_date = datetime.date(decade_num, 1, 1)
        end_date = datetime.date(decade_num + 10, 1, 1)
        infl_list = []
        for object in Inflation.objects.filter(date__range = [start_date, end_date]).values():
            little_dict = {}
            little_dict['date'] = str(object['date'])
            little_dict['rate'] = object['rate']
            infl_list.append(little_dict)
        json_data_infl = json.dumps(infl_list)
        un_list = []
        for object in Unemployment.objects.filter(date__range = [start_date, end_date]).values():
            little_dict = {}
            little_dict['date'] = str(object['date'])
            little_dict['rate'] = object['rate']
            un_list.append(little_dict)
        json_data_un = json.dumps(un_list)
        int_list = []
        for object in Interest.objects.filter(date__range = [start_date, end_date]).values():
            little_dict = {}
            little_dict['date'] = str(object['date'])
            little_dict['rate'] = object['rate']
            int_list.append(little_dict)
        json_data_int = json.dumps(int_list)
        context = super(Time_spans, self).get_context_data(**kwargs)
        context['name'] = stat
        context['json_data_infl'] = json_data_infl
        context['json_data_un'] = json_data_un
        context['json_data_int'] = json_data_int
        return context
