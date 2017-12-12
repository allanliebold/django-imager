"""Profile Models."""
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class ImageActiveProfile(models.Manager):
    """."""

    def get_queryset(self):
        """."""
        return super(ImageActiveProfile, self).get_queryset().filter(user__is_active=True)


class ImagerProfile(models.Model):
    """Imager Profile Model."""

    objects = models.Manager()
    active = ImageActiveProfile()

    CAMERAS = (
        ('NK', 'Nikon'),
        ('OL', 'Olympus'),
        ('GP', 'Go-Pro'),
    )

    SERVICES = (
        ('WD', 'Wedding'),
        ('GD', 'Graduation'),
        ('SP', 'Active/Sports'),
    )

    PHOTOGRAPHY = (
        ('BW', 'Black and White'),
        ('CL', 'Color')
    )

    website = models.URLField(default="example.com", null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    user = models.OneToOneField(User, related_name='profile', null=True, on_delete=models.CASCADE)
    fee = models.FloatField(default=0.0)
    phone = models.CharField(max_length=100, blank=True, null=True)

    camera = models.CharField(
        max_length=2,
        choices=CAMERAS,
        default='NK'
    )

    services = models.CharField(
        max_length=2,
        choices=SERVICES,
        default='WD'
    )

    photo_styles = models.CharField(
        max_length=2,
        choices=PHOTOGRAPHY,
        default='CL'
    )

    @property
    def is_active(self):
        """."""
        return self.user.is_active


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    """."""
    if kwargs['created']:
        profile = ImagerProfile(user=kwargs['instance'])
        profile.save()
