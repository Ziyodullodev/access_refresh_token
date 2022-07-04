from re import U
from django.db import models
from users.models import MyUser
# Create your models here.

class Ijara(models.Model):
    manzil = models.CharField(max_length=150)
    lokatsiya = models.CharField(max_length=150)
    malumot = models.TextField()
    ism = models.CharField(max_length=150)
    telefon = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    ijaranarxi = models.CharField(max_length=150)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    rasm = models.FileField(upload_to='media/', blank=True)

    def __str__(self):
        return f"{self.manzil}, ({self.ism})"