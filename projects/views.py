from django.shortcuts import render, redirect
from django.http import HttpResponse
import geopy.distance
from . import models
from django.contrib.auth.models import User

def filter_projects(projects, minduration, maxduration, maxdistance, latitude, longitude):
    output = []
    for project in projects:
        if minduration != None and project.duration < minduration:
            continue
        if maxduration != None and project.duration > maxduration:
            continue

        if latitude != None and maxdistance != None:
            user_location = (latitude, longitude)
            project_location = (project.latitude, project.longitude)
            distance = geopy.distance.distance(user_location, project_location).km

            if distance > maxdistance:
                continue

        output.append(project)
    return output


def homepage(request):
    projects = models.Project.objects.all()

    minduration = None
    if "minduration" in request.GET and request.GET["minduration"]:
        minduration = float(request.GET["minduration"])

    maxduration = None
    if "maxduration" in request.GET and request.GET["maxduration"]:
        maxduration = float(request.GET["maxduration"])

    maxdistance = None
    if "maxdistance" in request.GET and request.GET["maxdistance"]:
        maxdistance = float(request.GET["maxdistance"])

    latitude = None
    longitude = None
    if "latitude" in request.GET and request.GET["latitude"]:
        latitude = float(request.GET["latitude"])
        longitude = float(request.GET["longitude"])

    output = filter_projects(projects, minduration, maxduration, maxdistance, latitude, longitude)

    if latitude == None:
        latitude = 51.498833
        longitude = -0.175113

    return render(request, "projects/home.html", { "projects": output, "minduration": minduration, "maxduration": maxduration, "maxdistance": maxdistance, "latitude": latitude, "longitude": longitude })

def create_project(request):
    if request.method == "POST":
        project = models.Project()
        project.title = request.POST["title"]
        project.description = request.POST["description"]
        project.latitude = request.POST["latitude"]
        project.longitude = request.POST["longitude"]
        project.type = request.POST["type"]
        project.duration = float(request.POST["duration"])
        project.organiser = User.objects.all()[0]
        project.save()

        project = models.Project.objects.get(title=project.title)

        return redirect("/projects/" + str(project.id) + "/")

def view_project(request, project_id):
    project = models.Project.objects.get(pk=int(project_id))
    return render("projects/project.html", project)
