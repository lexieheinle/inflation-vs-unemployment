from django.shortcuts import render
from django.http import HttpResponse
from reports.models import Inflation, Unemployment, Interest
from django.views.generic import ListView

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def inflation(request, year, month):
    return HttpResponse("Hello, world. You're {} at the {} year on {}.".format("inflation", year, month))
  
def unemployment(request, year, month):
    return HttpResponse("Hello, world. You're {} at the {} year on {}.".format("unemployment", year, month))

def interest(request, year, month):
    return HttpResponse("Hello, world. You're {} at the {} year on {}.".format("interest", year, month))