from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def string3(request):
    return HttpResponse ('<marquee><h1> second app first string</h1></marquee>')

def string4(request):
    return HttpResponse ('<marquee><h1><i><u> SECOND  STRING  IN  SECOND  APP </i></u></h1></marquee>')