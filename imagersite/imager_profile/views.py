"""Views for top level app."""

from django.shortcuts import render
from imager_images.models import Album


def profile_request(request, username):
    """."""
    the_user = request.user
    albums = Album.objects.filter(user=the_user).count()
    private = Album.objects.filter(user=the_user, published='PRIVATE').count()
    public = Album.objects.filter(user=the_user, published='PUBLIC').count()
    shared = Album.objects.filter(user=the_user, published='SHARED').count()

    context = {
        'albums': albums,
        'username': username,
        'private': private,
        'shared': shared,
        'public': public
    }

    return render(request, 'imager_profile/profile.html', context)


def profile_view(request):
    """Render the profile for logged in user."""
    if request.user.is_authenticated:
        the_user = request.user

        private = Album.objects.filter(user=the_user,
                                       published='PRIVATE').count()
        public = Album.objects.filter(user=the_user,
                                      published='PUBLIC').count()
        shared = Album.objects.filter(user=the_user,
                                      published='SHARED').count()
        total_albums = Album.objects.filter(user=the_user).count()

    context = {
        'user': the_user,
        'total_albums': total_albums,
        'private': private,
        'shared': shared,
        'public': public
    }

    return render(request,
                  'imager_profile/profile_authenticated.html',
                  context)


def library_view(request):
    """View for image library."""
    return render(request, 'imager_profile/library.html')
