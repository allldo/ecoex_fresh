from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import timezone

from .models import News, Service


class NewsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return News.objects.all()

    def lastmod(self, obj):
        return obj.date

    def location(self, obj):
        return '/news/%s' % obj.slug


class ServiceSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Service.objects.all()

    def lastmod(self, obj):
        return timezone.now()

    def location(self, obj):
        return '/service/%s' % obj.title


class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['landing:main_page', 'landing:faq_fan', 'landing:contacts_fan', 'landing:pass_docs', 'landing:about_us']

    def location(self, item):
        return reverse(item)
