from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField

class Service(models.Model):
    title = models.CharField(max_length=45)
    image = models.ImageField(upload_to='services/')
    description = models.CharField(max_length=650)
    service_group = models.ForeignKey('ServiceGroup', on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('landing:service_detail', kwargs={'service_id': self.id})

    def __str__(self) -> str:
        return self.title


class ServiceGroup(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=150)
    answer = models.CharField(max_length=350)

    def __str__(self) -> str:
        return self.question


class News(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=75, unique=True, db_index=True, verbose_name="URL")
    image = models.ImageField(upload_to="news/", null=True)
    description = HTMLField()

    def save(self, *args, **kwargs):
        self.slug = self.slug
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
        
    def get_absolute_url(self):
        return reverse('landing:news_detail_page', kwargs={'news_slug': self.slug})


class PassDocs(models.Model):
    title = models.CharField(max_length=155)
    description = models.CharField(max_length=455)
    file_pdf = models.FileField(upload_to="docs")
    file_pdf_2 = models.FileField(upload_to="docs", null=True, blank=True)
    file_pdf_3 = models.FileField(upload_to="docs", null=True, blank=True)
    file_pdf_4 = models.FileField(upload_to="docs", null=True, blank=True)
    file_pdf_5 = models.FileField(upload_to="docs", null=True, blank=True)
    file_pdf_6 = models.FileField(upload_to="docs", null=True, blank=True)
    file_pdf_7 = models.FileField(upload_to="docs", null=True, blank=True)
    file_pdf_8 = models.FileField(upload_to="docs", null=True, blank=True)

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    text = HTMLField()
