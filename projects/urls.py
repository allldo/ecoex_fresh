from django.urls import path
from .views import *
urlpatterns = [
    path('project/<int:id>', project_detail, name='project_detail')
]