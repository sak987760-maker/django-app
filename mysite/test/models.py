from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

CATEGORY_CHOICES = [
    ('all',  'いろんなの'),
    ('diary', '日記'),
    ('volunteer', 'ボランティア'),
    ('research', '研究'),
    ('study', '勉強'),
    ('company', '企業'),
    ('work', '仕事'),
    ('hobby', '趣味'),
]

class User(AbstractUser):
    icon = models.ImageField(upload_to='icons/', blank=True, null=True)
    header = models.ImageField(upload_to='headers/', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='all')
    bio = models.CharField(max_length=100, blank=True)

class Ternal(models.Model):
    text = models.TextField(max_length=5000)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200, blank=True)
    