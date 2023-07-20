from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def string5(request):
    return HttpResponse ('<h1> LOVE YOU 3000 </h1>')

def string6(request):
    return HttpResponse ('<marquee><h1>Glory To Hanumana </h1></marquee>')