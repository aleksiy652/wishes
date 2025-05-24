from django.db import models
from django.contrib.auth.models import AbstractUser


class Polbzovatelb(AbstractUser):
    address = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)


class Wish(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField('Изображение', upload_to='images/', blank=True, null=True)
    uzer = models.ForeignKey(Polbzovatelb, on_delete=models.CASCADE, related_name="wishes_true")
