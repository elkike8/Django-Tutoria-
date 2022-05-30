from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1> Blog Home</h1>')

def test_area(request):
    return HttpResponse('<h1> Test Area</h1>')

def test_area_2(request):
    return HttpResponse('<h1>Second Test Area</h1>')