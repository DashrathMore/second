from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string1(request):
    return HttpResponse ('<h1> First String in First app </h1>')

def string2(request):
    return HttpResponse ('<h1><i> Second string in First app </i></h1>')