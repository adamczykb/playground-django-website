"""przedszkole URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from przedszkole import settings

urlpatterns = [
                  path('', include('website.urls')),
                  path('admin/', admin.site.urls),
                  path('summernote/', include('django_summernote.urls')),
                  path('gallery/', include('gallery.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('kalendarz/', include('schedule.urls')),
              ] + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'website.views.error_404_view'
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = "Przedszkole CMS"
admin.site.site_title = "CMS Bartosz Adamczyk"
admin.site.index_title = "Administacja treścią"
