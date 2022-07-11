from django.contrib.auth.models import User
from django.db import models


class Urls(models.Model):
    short_url = models.CharField(max_length=20)
    long_url = models.URLField('URL', unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
