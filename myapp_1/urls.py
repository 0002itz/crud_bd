from django.urls import path
from myapp_1 import views

urlpatterns = [
    path('', views.index),
]