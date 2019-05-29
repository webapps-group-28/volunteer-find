from django.shortcuts import render
from django.http import HttpResponse
from . import models

def home(request):
    return HttpResponse("this is the project page")

def project_search(request):
    projects = models.Project.objects.all()
    if minduration in request.GET:
        minduration = request.GET.minduration
    else:
        minduration = 0

    if maxduration in request.GET:
        maxduration = request.GET.maxduration
    else:
        maxduration = 1000

    output = []
    for project in projects:
        if project.duration >= minduration and project.duration <= maxduration:
            output.append(project)

    return render(request, "projects/search.html", { "projects": output })
