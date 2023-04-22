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
    title = "Project"
    project = Project.objects.all()
    return render(request,"projects.html", {
        'title': title
    })