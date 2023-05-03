# from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name


class Artist(models.Model):
    name = models.CharField(max_length=255)
    works = models.ManyToManyField('Work')

    # def __str__(self):
    #     return self.name


class Work(models.Model):
    LINK_TYPES = [
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('OT', 'Other')
    ]
    link = models.URLField()
    link_type = models.CharField(max_length=2, choices=LINK_TYPES)

    # def __str__(self):
    #     return link_type


