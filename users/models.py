from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    hours_environmental = models.IntegerField(default=0)
    hours_social = models.IntegerField(default=0)
    hours_educational = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def total_hours(self):
        return self.hours_environmental + self.hours_social + self.hours_educational

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
