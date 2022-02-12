from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=100)
