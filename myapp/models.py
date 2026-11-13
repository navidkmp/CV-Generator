from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField()
    degree = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    summary = models.TextField(max_length=2000)
    previous_work = models.TextField(max_length=2000)
    skills = models.CharField(max_length=200)