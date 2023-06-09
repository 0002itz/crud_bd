from django.shortcuts import get_object_or_404, render, HttpResponse
from .models import Project, Question



# Create your views here.
#def index(request):
#    title= "titel_index"
#    return render(request,"index.html", {
#        'title': title
#    })

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "index.html", context)

def project(request):
    projects= Project.objects.all()
    return render(request,"projects.html", {
        "projects": projects
    })

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)