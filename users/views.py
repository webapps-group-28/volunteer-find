from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def hours_to_level(hours):
    if hours <= 20:
        return "none"
    if hours <= 100:
        return "bronze"
    if hours <= 200:
        return "silver"
    return "gold"

def view_user_profile(request, username):
    user = User.objects.get(username=username)
    user.awards = []
    if hours_to_level(user.profile.total_hours()) != "none":
        user.awards.append(hours_to_level(user.profile.total_hours()) + " overall")
    if hours_to_level(user.profile.hours_environmental) != "none":
        user.awards.append(hours_to_level(user.profile.hours_environmental) + " environmental")
    if hours_to_level(user.profile.hours_social) != "none":
        user.awards.append(hours_to_level(user.profile.hours_social) + " social")
    if hours_to_level(user.profile.hours_educational) != "none":
        user.awards.append(hours_to_level(user.profile.hours_educational) + " educational")

    return render(request, "users/profile.html", { "user": user })

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "users/signup.html", {"form": form})
