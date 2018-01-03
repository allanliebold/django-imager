"""Views for top level app."""

import os
import random
from django.template import loader
from django.shortcuts import render
from imager_images.models import Photo
from .settings import BASE_DIR


def home_view(request):
    """Home page view."""
    public_photos = Photo.objects.filter(published='PUBLIC')
    return render(request, 'imagersite/index.html', context ={})
