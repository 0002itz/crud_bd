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

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)