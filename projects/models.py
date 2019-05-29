from django.db import models

class Project(models.Model):
    title = models.CharField()
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    type = models.CharField()
    duration = models.FloatField()
    date = models.DateField(auto_now_add=True)
