from django.contrib import admin
from django.urls import path
from landing import views
from django.contrib.sitemaps.views import sitemap
from .sitemap import NewsSitemap, ServiceSitemap, StaticSitemap

sitemaps = {
    'news':NewsSitemap,
    'services': ServiceSitemap,
    'static': StaticSitemap
}

urlpatterns = [
   path('', views.main_page, name='main_page'),
   path('news/<slug:news_slug>/', views.news_detail_page, name='news_detail_page'),
   path('faqs/', views.faq_list_page, name='faq_fan'),
   path('news/', views.news_list_page, name='news_fan'),
   path('contacts/', views.contacts, name='contacts_fan'),
   path('service/<int:service_id>', views.service_detail, name='service_detail'),
   path('services', views.services, name='services'),
   path('pass_docs', views.pass_docs, name='pass_docs'),
   path('about_us', views.about_us, name='about_us'),
   path('news_search', views.news_search, name='news_search'),
   path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

   # ajax
   path('form_valid', views.form_valid, name='form_valid')
]
