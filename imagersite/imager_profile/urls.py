"""imagersite URL Configuration."""
from django.conf.urls import url
from imager_profile.views import profile_view, profile_request, EditProfileView


urlpatterns = [
    url(r'^$', profile_view, name="profile_authenticated"),
    url(r'(?P<username>\w+)$', profile_request, name="profile"),
    url(r'^edit/$', EditProfileView.as_view(), name='profile_edit')
]
