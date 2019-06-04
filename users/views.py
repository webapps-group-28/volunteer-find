from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.contrib.auth.models import User

def view_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, "users/profile.html", { "user": user })
