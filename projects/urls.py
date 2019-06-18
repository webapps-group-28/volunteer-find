"""volunteerfind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    url(r'^create/$', views.create_project),
    url(r'^signup/$', views.project_signup),
    url(r'^certify/$', views.certify_project),
    url(r'^signupgroup/$', views.signup_group),
    url(r'^myprojects/$', views.my_projects),
    url(r'^count/(?P<project_id>[\d]+)/$', views.project_count, name="project_count"),
    url(r'^(?P<project_id>[\d]+)/$', views.view_project, name="view_project")
]
