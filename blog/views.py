from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "blog/home.html")


def test_area(request):
    return render(request, "blog/test_area.html")


def homie(request):
    return render(request, "blog/the_homie_page.html")
