from django.db import models
from django.urls import reverse

class Service(models.Model):
    title = models.CharField(max_length=45)
    image = models.ImageField(upload_to='services/')
    description = models.CharField(max_length=650)

    def __str__(self) -> str:
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=150)
    answer = models.CharField(max_length=350)

    def __str__(self) -> str:
        return self.question

class News(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=75)
    image = models.ImageField(upload_to="news/", null=True)
    description = models.TextField()
    
    def get_absolute_url(self):
        return reverse("news_detail_page", args=[self.slug])
    

    def __str__(self) -> str:
        return self.title