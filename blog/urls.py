from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("test/", views.test_area, name="test-area"),
    path("homie/", views.homie, name="homie-page"),
]
