from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
