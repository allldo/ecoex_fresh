from django.contrib import admin
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import  settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(("landing.urls", 'landing'), namespace='landing')),

] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

