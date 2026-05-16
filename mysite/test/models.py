from django.db import models

# Create your models here.
class Ternal(models.Model):
    text = models.CharField(max_length=100)