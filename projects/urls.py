from django.urls import path
from .views import *
urlpatterns = [
    path('', air_quality, name='project_detail')
]