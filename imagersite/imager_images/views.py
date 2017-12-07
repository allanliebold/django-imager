"""Views for imager_images."""
from django.views.generic import DetailView
from django.http import Http404
from imager_images.models import Photo


class ImageView(DetailView):
    """Single image view."""

    template = 'imager_images/photo_detail.html'
    model = Photo
    image_id = 'id'

    def get_object(self):
        """Get photo and check its public."""
        photo = super(ImageView, self).get_object()
        if photo.published != 'PUBLIC':
            raise Http404('This Photo is not Public')

        return photo
