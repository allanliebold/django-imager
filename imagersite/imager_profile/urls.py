"""imagersite URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.profile_view, name="profile"),
    url(r'^(?P<username>.*)$', views.profile_view, name="profile")
]
