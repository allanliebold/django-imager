"""Views for top level app."""

from django.shortcuts import get_object_or_404, redirect, render
from imager_profile.models import ImagerProfile
from imager_images.models import Album, Photo


def profile_view(request, username=None):
    """Render the profile for a user."""
    owner = False
    if not username:
        username = request.user.get_username()
        owner = True
        if username == '':
            return redirect('home')

    profile = get_object_or_404(ImagerProfile, user__username=username)
    photos = Photo.objects.filter(user__username=username)
    albums = Album.objects.filter(user__username=username)

    if not owner:
        photos = photos.filter(published='PUBLIC')
        albums = albums.filter(published='PUBLIC')

    context = {
        'owner': owner,

        'username': profile.user.username,
        'camera': profile.get_camera_display(),
        # 'email': profile.user.email,
        'website': profile.website,
        'fee': "{:,.2f}".format(profile.fee) if profile.fee else 0,
        'location': profile.location,
        'phone': profile.phone,
        'services': profile.get_services_list(),
        'photo_styles': profile.get_photo_styles_list(),

    #     'albums': [album.title for album in albums.iterator()],
    #     'album_ids': [album.id for album in albums.iterator()],
    #     'album_private_count': albums.filter(published='PRIVATE').count(),
    #     'album_public_count': albums.filter(published='PUBLIC').count(),

    #     'photos': [photo.title for photo in photos.iterator()],
    #     'photos_ids': [photo.id for photo in photos.iterator()],
    #     'photo_private_count': photos.filter(published='PRIVATE').count(),
    #     'photo_public_count': photos.filter(published='PUBLIC').count()
    }
    return render(request, 'imager_profile/profile.html', context)

