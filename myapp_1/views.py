from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    title= "titel_index"
    return render(request,"index.html", {
        'title': title
    })