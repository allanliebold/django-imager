from django.db import models
from django.contrib.auth.models import User


class ImageActiveProfile(models.Manager):
    """."""

    def get_queryset(self):
        """."""
        super(ImageActiveProfile, self).get_queryset().filter(is_active=True)


class ImagerProfile(models.Model):
    """Imager Profile Model."""

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

    website = models.URLField(default="example.com")
    location = models.CharField(max_length=200, blank=True, null=True)
    user = models.OneToOneField(User, related_name='profile')
    fee = models.FloatField(default=0.0)
    phone = models.CharField(default="555-555-5555", max_length=100)

    camera = models.CharField(
        max_length=2,
        choices=CAMERAS,
        default='NIKON'
    )

    services = models.CharField(
        max_length=2,
        choices=SERVICES,
        default='WEDDING'
    )

    photo_styles = models.CharField(
        max_length=2,
        choices=PHOTOGRAPHY,
        default='CL'
    )

    active = ImageActiveProfile()

    @property
    def is_active(self):
        """."""
        return self.user.is_active
