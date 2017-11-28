from django.db import models
from imager_profile.models import ImagerProfile
from multiselectfield import MultiSelectField

class Photo(models.Model):
    """."""

    user = models.ForeignKey(ImagerProfile, related_name='photo')
    image = models.ImageField(upload_to='documents/%Y/%m/%d')
    title = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField()

    PUBLISHED = [
        ('PRIVATE', 'Private'),
        ('SHARED', 'Shared'),
        ('PUBLIC', 'Public')
    ]

    published = model.CharField(
        max_length=10,
        choices=PUBLISHED,
        blank=True
    )



class Album(models.Model):
    """Album Model for pictures."""

    user = models.ForeignKey(ImagerProfile, related_name='album')
    photo = models.ManyToManyField(Photo)
    title = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField()

    PUBLISHED = [
        ('PRIVATE', 'Private'),
        ('SHARED', 'Shared'),
        ('PUBLIC', 'Public')
    ]

    published = model.CharField(
        max_length=10,
        choices=PUBLISHED,
        blank=True
    )
