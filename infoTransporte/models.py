from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=40)
    dni = models.CharField(primary_key=True, max_length=20)
    nombreUser = models.CharField(unique=True, max_length=20)

