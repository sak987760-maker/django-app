from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    icon = models.ImageField(
        upload_to='icons/',
        blank=True,
        null=True,
    )
    header = models.ImageField(upload_to='headers/', blank=True, null=True)

class Ternal(models.Model):
    text = models.TextField(max_length=5000)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)