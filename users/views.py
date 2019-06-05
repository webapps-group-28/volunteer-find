from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def hours_to_level(hours):
    if hours <= 20:
        return None
    if hours <= 100:
        return "Bronze"
    if hours <= 200:
        return "Silver"
    return "Gold"

def view_user_profile(request, username):
    user = User.objects.get(username=username)
    user.awards = []
    if hours_to_level(user.profile.total_hours()) != None:
        user.awards.append((hours_to_level(user.profile.total_hours()), "Commitment"))
    if hours_to_level(user.profile.hours_environmental) != None:
        user.awards.append((hours_to_level(user.profile.hours_environmental), "Environmental"))
    if hours_to_level(user.profile.hours_social) != None:
        user.awards.append((hours_to_level(user.profile.hours_social), "Social"))
    if hours_to_level(user.profile.hours_educational) != None:
        user.awards.append((hours_to_level(user.profile.hours_educational), "Educational"))

    return render(request, "users/profile.html", { "user": user })

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("view_user_profile", username=user.username)
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("/")

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if "firstname" in request.POST:
                user.first_name = request.POST["firstname"]
            if "lastname" in request.POST:
                user.last_name = request.POST["lastname"]
            if "bio" in request.POST:
                user.profile.bio = request.POST["bio"]
            if "email" in request.POST:
                user.profile.email = request.POST["email"]
            if "phone" in request.POST:
                user.profile.phone = request.POST["phone"]
            user.profile.type = request.POST["type"]
            user.save()
            login(request, user)
            return redirect("view_user_profile", username=user.username)
    else:
        form = UserCreationForm()
    return render(request, "users/signup.html", {"form": form})
