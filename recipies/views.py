from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def recipies(request):
    return render(request, "recipies/recipies.html")
