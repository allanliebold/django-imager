from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ImageActiveProfile(models.Manager):
    """."""

    def get_queryset(self):
        """."""
        super(ImageActiveProfile, self).get_queryset().filter(is_active=True)


class ImagerProfile(models.Model):
    location = models.CharField(max_length=200, blank=True, null=True)
    user = models.OneToOneField(User, related_name='profile')

    active = ImageActiveProfile()

    @property
    def is_active(self):
        """."""
        return self.user.is_active
