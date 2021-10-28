from django.contrib import admin
from django.urls import path
from landing import views
urlpatterns = [
   path('', views.main_page, name='main_page'),
   path('news/<slug:slug>', views.news_detail_page, name='news_detail_page')
]
