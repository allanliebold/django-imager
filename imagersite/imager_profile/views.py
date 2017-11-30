"""Views for top level app."""

from django.template import loader
from django.shortcuts import render


def profile_view(request):
    """Profile page view."""
    return render(request, 'imager_profile/profile.html', {
        # 'rand_images': rand_images
        })

