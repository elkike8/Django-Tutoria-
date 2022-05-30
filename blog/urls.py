from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('test', views.test_area, name='test-area'),
    path('test2', views.test_area_2, name='test-area-2'),
]
