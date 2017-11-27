"""imagersite URL Configuration
"""

from django.conf.urls import include, url
from django.contrib import admin
from imagersite import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_view, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
]
