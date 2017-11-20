from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class LenderProfile(models.Model):
    location = models.CharField(max_length=200, blank=True null=True)
    user = models.OneToOneField(User, related_name='profile')
