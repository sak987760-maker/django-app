from django.db import models

# Create your models here.
class Ternal(models.Model):
    text = models.TextField(max_length=5000)
