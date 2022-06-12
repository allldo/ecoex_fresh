from django.urls import path
from .views import *
urlpatterns = [
    path('qwe', air_quality, name='air_qual')
]