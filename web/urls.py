from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from res import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('',include('django.contrib.auth.urls')),
    url(r'^res/', include('res.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +\
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
