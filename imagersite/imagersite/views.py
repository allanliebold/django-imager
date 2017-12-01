"""Views for top level app."""

import os
import random
from django.template import loader
from django.shortcuts import render
from .settings import BASE_DIR


def home_view(request):
    """Home page view."""
    images_path = os.path.join(BASE_DIR, 'MEDIA/images')
    rand_images = random.choice(['images/' + f for f in os.listdir(images_path)])
    return render(request, 'imagersite/index.html', {
        'rand_images': rand_images}
                  )

