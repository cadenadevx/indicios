from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    cargo = models.CharField(max_length=100, verbose_name='Cargo')
    dependencia = models.CharField(max_length=100, verbose_name='Dependencia')
    telefono = models.CharField(max_length=10, verbose_name='Teléfono')

    def __str__(self):
        return self.username