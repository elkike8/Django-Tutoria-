from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def recipies(request):
    return HttpResponse("<h1>Recepies</hi>")