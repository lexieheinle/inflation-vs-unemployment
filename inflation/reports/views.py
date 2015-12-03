from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from reports.models import Inflation, Unemployment, Interest
from django.views.generic import ListView


# Create your views here.
def index(request):
    return render_to_response('main.html')
  
def inflationOverview(request):
    stat = "Inflation"
    objects = Inflation
    dictionaries = {'name': stat}
    return render_to_response('stat.html')

def inflation(request, year, month):
    return HttpResponse("Hello, world. You're {} at the {} year on {}.".format("inflation", year, month))
  
def unemployment(request, year, month):
    return HttpResponse("Hello, world. You're {} at the {} year on {}.".format("unemployment", year, month))

def interest(request, year, month):
    return HttpResponse("Hello, world. You're {} at the {} year on {}.".format("interest", year, month))