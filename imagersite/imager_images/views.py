"""Views for imager_images."""
from django.views.generic import DetailView, ListView, CreateView
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from imager_images.models import Photo, Album


class ImageView(DetailView):
    """Single image view."""

    template = 'imager_images/photo_detail.html'
    model = Photo
    image_id = 'id'

    def get_object(self):
        """Get photo and check its public."""
        photo = super(ImageView, self).get_object()
        if photo.published != 'PUBLIC':
            if photo.user.username != self.request.user.get_username():
                raise Http404('This Photo does not belong to you')
        return photo


class CreateAlbumView(CreateView):
    """."""

    template_name = 'imager_images/album_form.html'
    model = Album
    success_url = reverse_lazy('library')
    fields = ['user', 'photo', 'title', 'description']


class CreateImageView(CreateView):
    """."""

    template_name = 'imager_images/image_form.html'
    model = Photo
    success_url = reverse_lazy('library')
    fields = ['user', 'image', 'title', 'description']

    def form_valid(self, form):
        """."""
        # import pdb; pdb.set_trace()
        form.instance.user = User.objects.get(username='superman')
        return super(CreateImageView, self).form_valid(form)
