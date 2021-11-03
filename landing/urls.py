from django.contrib import admin
from django.urls import path
from landing import views
urlpatterns = [
   path('', views.main_page, name='main_page'),
   path('news/<slug:news_slug>/', views.news_detail_page, name='news_detail_page'),
   path('faqs/', views.faq_list_page, name='faq_fan'),
   path('news/', views.news_list_page, name='news_fan'),
   path('contacts/', views.contacts, name='contacts_fan'),
]
