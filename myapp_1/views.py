from django.shortcuts import render
from django.shortcuts import HttpResponse
from myapp_1 import views


# Create your views here.
def hello(request):
    return HttpResponse("<h2>Hello word</h2>")