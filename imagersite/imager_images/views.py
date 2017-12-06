"""Views for imager_images."""
from django.shortcuts import render
from imager_images.models import Photo


def image_view(request, pk):
    """View for single images."""
    image = Photo.objects.get(pk=pk)
    title = image.title
    description = image.description
    username = image.user.username

    context = {
        'image': image,
        'description': description,
        'title': title,
        'username': username,
        'pk': pk
    }

    return render(request, 'imager_images/image.html', context)
