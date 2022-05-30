from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipies, name='recipie-home'),
]
