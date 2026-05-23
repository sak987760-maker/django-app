from django.db import models

# Create your models here.
class Ternal(models.Model):
    text = models.TextField(max_length=5000)
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    icon = models.ImageField(
        upload_to='icons/',  
        default='icons/default.png',  
        blank=True
    )