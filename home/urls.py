from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="landing-page"),
    path("homie/", views.home, name="homie-page"),
]
