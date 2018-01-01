"""Views for top level app."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from imager_images.models import Album
from imager_profile.forms import ProfileForm
from .models import ImagerProfile


def profile_request(request, username):
    """Public profile view."""
    if User.objects.filter(username=username).exists():
        the_user = User.objects.get(username=username)
        albums = Album.objects.filter(user=the_user).count()
        private = Album.objects.filter(user=the_user, published='PRIVATE').count()
        public = Album.objects.filter(user=the_user, published='PUBLIC').count()
        shared = Album.objects.filter(user=the_user, published='SHARED').count()

        context = {
            'albums': albums,
            'username': the_user.username,
            'private': private,
            'shared': shared,
            'public': public,
            'user_exists': True
        }

    else:
        context = {
            'user_exists': False,
            'username': username
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
    else:
        context = {}

    return render(request,
                  'imager_profile/profile_authenticated.html',
                  context)


def library_view(request):
    """View for image library."""
    if request.user.is_authenticated:
        the_user = request.user

        albums = Album.objects.filter(user=the_user)
        context = {'the_user': the_user,
                   'albums': albums}
    return render(request, 'imager_profile/library.html', context)


class EditProfileView(LoginRequiredMixin, UpdateView):
    """Class based to view to generate for user to update profile."""

    model = ImagerProfile
    fields = [
        'phone',
        'website',
        'location',
        'fee',
        'camera',
        'services',
        'photo_styles']
    template_name_suffix = '_update_form'
    context_object_name = 'profile'
    success_url = reverse_lazy('profile_authenticated')

    def get_object(self):
        """Populate form."""
        return self.request.user.profile
