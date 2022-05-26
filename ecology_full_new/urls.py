from django.contrib import admin
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import  settings
handler404 = 'landing.views.handler404'
handler500 = 'landing.views.handler500'
handler403 = 'landing.views.handler403'
if settings.DEBUG:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include(("landing.urls", 'landing'), namespace='landing')),
        path('air_quality/', include(("projects.urls", 'projects'), namespace='projects')),
    ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include(("landing.urls", 'landing'), namespace='landing')),
        path('air_quality/', include(("projects.urls", 'projects'), namespace='projects')),
]