"""Views for imager_images."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, CreateView
from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from imager_images.models import Photo, Album
from imager_images.forms import PhotoForm


class ImageView(DetailView):
    """Single image view."""

    template = 'imager_images/photo_detail.html'
    model = Photo

    def get_object(self):
        """Get photo and check its public."""
        photo = super(ImageView, self).get_object()
        if photo.published != 'PUBLIC':
            if photo.user.username != self.request.user.get_username():
                raise Http404('This Photo does not belong to you')
        return photo


class AlbumView(DetailView):
    """Single Album view."""

    template = 'imager_images/album_detail.html'
    model = Album

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context['object'] != 'PUBLIC':
            if context['object'].user.username != self.request.user.get_username():
                raise Http404('This Photo does not belong to you')

        photo = context['object'].photo.first().image
        context['photo'] = photo
        # import pdb; pdb.set_trace()
        return context


class CreateAlbumView(CreateView):
    """."""

    template_name = 'imager_images/album_form.html'
    model = Album
    success_url = reverse_lazy('library')
    fields = ['photo', 'title', 'description', 'published']

    def form_valid(self, form):
        """."""
        logged_in_user = self.request.user.get_username()
        form.instance.user = User.objects.get(username=logged_in_user)
        return super(CreateAlbumView, self).form_valid(form)


class CreateImageView(CreateView):
    """."""

    template_name = 'imager_images/image_form.html'
    model = Photo
    success_url = reverse_lazy('library')
    fields = ['image', 'title', 'description', 'published']

    def form_valid(self, form):
        """."""
        # import pdb; pdb.set_trace()
        logged_in_user = self.request.user.get_username()
        form.instance.user = User.objects.get(username=logged_in_user)
        return super(CreateImageView, self).form_valid(form)


class EditAlbumView(UpdateView):
    """."""

    template_name = 'imager_images/album_edit.html'
    model = Album
    success_url = reverse_lazy('library')
    fields = ['photo', 'title', 'description', 'published']

    def get(self, request, *args, **kwargs):
        """."""
        if request.user.username == Album.objects.get(id=self.kwargs['pk']).user.username:
            return super(EditAlbumView, self).get(request, *args, **kwargs)
        return redirect(reverse_lazy('home'))

    def form_valid(self, form):
        """."""
        logged_in_user = self.request.user.get_username()
        form.instance.user = User.objects.get(username=logged_in_user)
        return super(EditAlbumView, self).form_valid(form)


class EditImageView(LoginRequiredMixin, UpdateView):
    """."""

    template_name = 'imager_images/image_edit.html'
    model = Photo
    success_url = reverse_lazy('library')
    form_class = PhotoForm

    def get(self, request, *args, **kwargs):
        """."""
        if request.user.username == Photo.objects.get(id=self.kwargs['pk']).user.username:
            return super(EditImageView, self).get(request, *args, **kwargs)
        return redirect(reverse_lazy('home'))

    def form_valid(self, form):
        """."""
        logged_in_user = self.request.user.get_username()
        form.instance.user = User.objects.get(username=logged_in_user)
        return super(EditImageView, self).form_valid(form)
