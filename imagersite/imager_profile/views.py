"""Views for top level app."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.shortcuts import render, redirect
from imager_images.models import Album
from django.urls import reverse_lazy
from imager_profile.forms import ProfileForm
from .models import ImagerProfile


def profile_request(request, username):
    """Public profile view."""
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
                  'imager_profile/profile_edit.html',
                  context)


def library_view(request):
    """View for image library."""
    if request.user.is_authenticated:
        the_user = request.user

        albums = Album.objects.filter(user=the_user)
        an_album = albums[0]
        context = {'the_user': the_user,
                   'an_album': an_album,
                   'albums': albums}
    return render(request, 'imager_profile/library.html', context)


class EditProfileView(LoginRequiredMixin, UpdateView):
    """."""

    template_name = 'imager_images/profile_edit.html'
    model = ImagerProfile
    success_url = reverse_lazy('profile')
    form_class = ProfileForm

    def get(self, request, *args, **kwargs):
        """."""
        if request.user.username == ImagerProfile.objects.get(id=self.kwargs['pk']).user.username:
            return super(EditProfileView, self).get(request, *args, **kwargs)
        return redirect(reverse_lazy('home'))

    def form_valid(self, form):
        """."""
        form.instance.user = self.request.user
        return super(EditProfileView, self).form_valid(form)
