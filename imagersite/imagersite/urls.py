"""imagersite URL Configuration."""

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from imagersite import views
from django.contrib.auth import views as auth_views
from imagersite import settings
from imager_profile.views import library_view
from imager_images.views import AlbumView, ImageView, CreateAlbumView, CreateImageView
from imager_images.views import EditImageView, EditAlbumView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_view, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^profile/', include('imager_profile.urls')),
    url(r'^images/library/$', library_view, name='library'),
    url(r'^images/photos/(?P<pk>\d+)/$', ImageView.as_view(), name='single_image'),
    url(r'^images/albums/(?P<pk>\d+)/$', AlbumView.as_view(), name='single_album'),
    url(r'^images/albums/add/$', CreateAlbumView.as_view(), name='create_album'),
    url(r'^images/photos/add/$', CreateImageView.as_view(), name='create_image'),
    url(r'^images/albums/(?P<pk>\d+)/edit$', EditAlbumView.as_view(), name='edit_album'),
    url(r'^images/photos/(?P<pk>\d+)/edit$', EditImageView.as_view(), name='edit_photo'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
