from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from reports.models import Inflation, Unemployment, Interest
from django.views.generic import ListView
import json
import datetime

# Create your views here.
def index(request):
    stat = 'Index'
    dictionaires = {'name': stat}
    return render_to_response('main.html', dictionaires)
  
def unemploymentData():
  data = list(Unemployment.objects.all().values())
  return JsonResponse(data, safe=False)
  
def unemploymentOverview(request):
    stat = "Unemployment"
    objects = Unemployment.objects.all()
    myList = []
    for object in Unemployment.objects.all().values():
      littleDict = {}
      littleDict['date'] = str(object['date'])
      littleDict['rate'] = object['rate']
      myList.append(littleDict)
    json_data = json.dumps(myList)
    dictionaries = {'name': stat, 'objects': objects, 'json_data': json_data}
    return render_to_response('stat.html', dictionaries)
  
def interestOverview(request):
    stat = "Interest"
    objects = Interest.objects.all()
    myList = []
    for object in Interest.objects.all().values():
      littleDict = {}
      littleDict['date'] = str(object['date'])
      littleDict['rate'] = object['rate']
      myList.append(littleDict)
    json_data = json.dumps(myList)
    dictionaries = {'name': stat, 'objects': objects, 'json_data': json_data}
    return render_to_response('stat.html', dictionaries)

def inflationOverview(request):
    stat = "Inflation"
    objects = Inflation.objects.all()
    myList = []
    for object in Inflation.objects.all().values():
      littleDict = {}
      littleDict['date'] = str(object['date'])
      littleDict['rate'] = object['rate']
      myList.append(littleDict)
    json_data = json.dumps(myList)
    dictionaries = {'name': stat, 'objects': objects, 'json_data': json_data}
    return render_to_response('stat.html', dictionaries)
  
def timeSpans(request, decadeNum):
  decadeNum = int(decadeNum)
  stat = "{}s".format(decadeNum)
  startDate = datetime.date(decadeNum, 1, 1)
  endDate = datetime.date(decadeNum + 10, 1, 1)
  #inflationObjs = Inflation.objects.filter(date__range = [startDate, endDate])
  inflList = []
  for object in Inflation.objects.filter(date__range = [startDate, endDate]).values():
      littleDict = {}
      littleDict['date'] = str(object['date'])
      littleDict['rate'] = object['rate']
      inflList.append(littleDict)
  json_data_infl = json.dumps(inflList)
  unList = []
  for object in Unemployment.objects.filter(date__range = [startDate, endDate]).values():
      littleDict = {}
      littleDict['date'] = str(object['date'])
      littleDict['rate'] = object['rate']
      unList.append(littleDict)
  json_data_un = json.dumps(unList)
  intList = []
  for object in Interest.objects.filter(date__range = [startDate, endDate]).values():
      littleDict = {}
      littleDict['date'] = str(object['date'])
      littleDict['rate'] = object['rate']
      intList.append(littleDict)
  json_data_int = json.dumps(intList)
  dictionaires = {'name': stat, 'json_data_infl': json_data_infl, 'json_data_un': json_data_un, 'json_data_int': json_data_int}
  return render_to_response('time.html', dictionaires)

def source(request):
  stat = 'Source'
  dictionaires = {'name': stat}
  return render_to_response('source.html', dictionaires)
  
def unemployment(request, year, month):
    return HttpResponse("Hello, world. You're {} at the {} year on {}.".format("unemployment", year, month))

def interest(request, year, month):
    return HttpResponse("Hello, world. You're {} at the {} year on {}.".format("interest", year, month))

def inflation(request, year, month):
    return HttpResponse("Hello, world. You're {} at the {} year on {}.".format("inflation", year, month))