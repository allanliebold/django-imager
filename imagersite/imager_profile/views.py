"""Views for top level app."""

from django.shortcuts import get_object_or_404, redirect, render
from imager_profile.models import ImagerProfile
from imager_images.models import Album, Photo


def profile_request(request, username):
    """."""
    # profile = get_object_or_404(ImagerProfile, user__username=username)
    albums = Album.objects.filter(published='PUBLIC').filter(user__user__username=username)
    context = {
         'albums': albums,
         'user': username
    }
    return render(request, 'imager_profile/profile.html', context)


def profile_view(request):
    """Render the profile for logged in user."""
    if request.user.is_authenticated:
        the_user = request.user.username
        albums = Album.objects.filter(user__user__username=the_user)
    context = {
        'albums': albums,
        'user': the_user
    }
    return render(request, 'imager_profile/profile.html', context)
