from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.contrib.auth.models import User

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
    if hours_to_level(user.profile.total_hours) != "none":
        user.awards.append(hours_to_level(user.profile.total_hours) + " overall")
    if hours_to_level(user.profile.hours_environmental) != "none":
        user.awards.append(hours_to_level(user.profile.hours_environmental) + " environmental")
    if hours_to_level(user.profile.hours_social) != "none":
        user.awards.append(hours_to_level(user.profile.hours_social) + " social")
    if hours_to_level(user.profile.hours_educational) != "none":
        user.awards.append(hours_to_level(user.profile.hours_educational) + " educational")

    return render(request, "users/profile.html", { "user": user })
