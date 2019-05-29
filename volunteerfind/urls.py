from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views
from projects import views as project_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', projects_views.project_search),
    url(r'^projects/', include('projects.urls'))
]
