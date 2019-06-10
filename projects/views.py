from django.shortcuts import render, redirect
from django.http import HttpResponse
import geopy.distance
from . import models
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def project_signup(request):
    if request.method == "POST":
        volunteerEntry = models.Volunteer()
        volunteerEntry.user = request.user
        volunteerEntry.project = Project.objects.get(id=int(request.POST["project_id"]))
        volunteerEntry.save()

def filter_projects(projects, minduration, maxduration, maxdistance, latitude, longitude):
    output = []

    if latitude == None:
        latitude = 51.498833
    if longitude == None:
        longitude = -0.175113

    for project in projects:
        if minduration != None and project.duration < minduration:
            continue
        if maxduration != None and project.duration > maxduration:
            continue

        user_location = (latitude, longitude)
        project_location = (project.latitude, project.longitude)
        distance = geopy.distance.distance(user_location, project_location).km

        if maxdistance != None and distance > maxdistance:
            continue

        project.distance = int(distance)

        output.append(project)
    return output


def homepage(request):
    projects = models.Project.objects.all()
    for project in projects:
        project.duration = int(project.duration)

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
    output.sort(key=lambda project : project.distance)

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
    project.duration = int(project.duration)
    project.volunteers = []
    volunteerEntries = models.Volunteer.objects.all()
    for entry in volunteerEntries:
        if int(entry.project.id) == int(project_id):
            project.volunteers.append(entry.user)
    project.num_volunteers = len(project.volunteers)
    return render(request, "projects/project.html", { "project": project })
