from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=100,blank=False)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    donador = models.BooleanField(default=False)