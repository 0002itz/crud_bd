from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Project


# Create your views here.
def index(request):
    title= "titel_index"
    return render(request,"index.html", {
        'title': title
    })

def project(request):
    projects= Project.objects.all()
    return render(request,"projects.html", {
        "projects": projects
    })