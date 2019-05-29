from django.shortcuts import render
from django.http import HttpResponse
from . import models

def home(request):
    return HttpResponse("this is the project page")

def project_search(request):
    projects = models.Project.objects.all()
    return render(request, "projects/search.html", { "projects": projects })
