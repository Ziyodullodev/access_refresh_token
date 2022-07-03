from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    # first_name = models.CharField(max_length=255, blank=True)
    # last_name = models.CharField(max_length=255, blank=True)
    first_name = None
    last_name = None
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
