from django.shortcuts import render
from django.http import HttpResponse
from reports.models import Inflation
from django.views.generic import ListView

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def inflation(request, year, month):
    return HttpResponse("Hello, world. You're at the {}.".format(year))