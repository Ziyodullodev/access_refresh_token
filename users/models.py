from django.db import models


class MyUser(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255, choices=(("Ijaraga qo'yuvchi", "Ijaraga qo'yuvchi"),("Ijaraga oluvchi", "Ijaraga oluvchi")))

    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.email