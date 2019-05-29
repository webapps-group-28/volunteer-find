from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    type = models.CharField(max_length=100)
    duration = models.FloatField()
    date = models.DateField(auto_now_add=True)
