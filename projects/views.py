from django.shortcuts import render
from django.http import HttpResponse
import geopy.distance
from . import models

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


def project_search(request):
    projects = models.Project.objects.all()

    minduration = None
    if "minduration" in request.GET:
        minduration = float(request.GET["minduration"])

    maxduration = None
    if "maxduration" in request.GET:
        maxduration = float(request.GET["maxduration"])

    maxdistance = None
    if "maxdistance" in request.GET:
        maxdistance = float(request.GET["maxdistance"])

    latitude = None
    longitude = None
    if "latitude" in request.GET:
        latitude = float(request.GET["latitude"])
        longitude = float(request.GET["longitude"])

    output = filter_projects(projects, minduration, maxduration, maxdistance, latitude, longitude)

    return render(request, "projects/search.html", { "projects": output })
