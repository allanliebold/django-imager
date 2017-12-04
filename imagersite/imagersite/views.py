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
    context = {
        'pic1': random.choice(public_photos).image.url,
        'pic2': random.choice(public_photos).image.url,
        'pic3': random.choice(public_photos).image.url,
        'pic4': random.choice(public_photos).image.url,
        'pic5': random.choice(public_photos).image.url
    }
    # import pdb; pdb.set_trace()
    return render(request, 'imagersite/index.html', context)
