from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Account(AbstractUser):
    displayname = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
