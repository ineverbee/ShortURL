from django.db import models
from django.contrib.auth import get_user_model


class ShortURL(models.Model):
    url = models.URLField(max_length=300)
    custom_url = models.CharField(max_length=50)