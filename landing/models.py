from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=45)
    image = models.ImageField(upload_to='services/')
    description = models.CharField(max_length=650)

    def __str__(self) -> str:
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=150)
    answer = models.CharField(max_length=350)


class News(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()