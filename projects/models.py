from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=220)
    description = models.TextField
    description_in_front = models.CharField(max_length=120)
    price = models.CharField(max_length=15)
    image = models.ImageField(upload_to='project/')