from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from reports.models import Inflation, Unemployment, Interest
from django.views.generic import ListView
import json

# Create your views here.
def index(request):
    return render_to_response('main.html')
  
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

def inflation(request, year, month):
    return HttpResponse("Hello, world. You're {} at the {} year on {}.".format("inflation", year, month))
  
def unemployment(request, year, month):
    return HttpResponse("Hello, world. You're {} at the {} year on {}.".format("unemployment", year, month))

def interest(request, year, month):
    return HttpResponse("Hello, world. You're {} at the {} year on {}.".format("interest", year, month))