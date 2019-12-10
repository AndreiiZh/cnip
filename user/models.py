from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.

class User(models.Model):
    fist_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=128)
    phone_number = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.fist_name} {self.last_name}'
