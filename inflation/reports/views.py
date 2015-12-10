from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from reports.models import Inflation, Unemployment, Interest
from django.views.generic import ListView
import json
import datetime

# Create your views here.
def index(request):
    '''Render index page'''
    stat = 'Index'
    dictionaires = {'name': stat}
    return render_to_response('main.html', dictionaires)
   
def unemployment_overview(request):
    '''Render unemployment page'''
    stat = "Unemployment"
    objects = Unemployment.objects.all()
    my_list = []
    for object in Unemployment.objects.all().values():
      little_dict = {}
      little_dict['date'] = str(object['date'])
      little_dict['rate'] = object['rate']
      my_list.append(little_dict)
    json_data = json.dumps(my_list)
    dictionaries = {'name': stat, 'objects': objects, 'json_data': json_data}
    return render_to_response('stat.html', dictionaries)
  
def interest_overview(request):
    '''Render interest page'''
    stat = "Interest"
    objects = Interest.objects.all()
    my_list = []
    for object in Interest.objects.all().values():
      little_dict = {}
      little_dict['date'] = str(object['date'])
      little_dict['rate'] = object['rate']
      my_list.append(little_dict)
    json_data = json.dumps(my_list)
    dictionaries = {'name': stat, 'objects': objects, 'json_data': json_data}
    return render_to_response('stat.html', dictionaries)

def inflation_overview(request):
    '''Render inflation page'''
    stat = "Inflation"
    objects = Inflation.objects.all()
    my_list = []
    for object in Inflation.objects.all().values():
      little_dict = {}
      little_dict['date'] = str(object['date'])
      little_dict['rate'] = object['rate']
      my_list.append(little_dict)
    json_data = json.dumps(my_list)
    dictionaries = {'name': stat, 'objects': objects, 'json_data': json_data}
    return render_to_response('stat.html', dictionaries)
  
def time_spans(request, decade_num):
  '''Render decade pages'''
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
  dictionaires = {'name': stat, 'json_data_infl': json_data_infl, 'json_data_un': json_data_un, 'json_data_int': json_data_int}
  return render_to_response('time.html', dictionaires)

def source(request):
  '''Render source page'''
  stat = 'Source'
  dictionaires = {'name': stat}
  return render_to_response('source.html', dictionaires)
