from django.db import models

# Create your models here.
class Curso(models.Model):
    profesor = models.CharField(max_length=20)
    curso = models.CharField(max_length=20)
    codigo = models.IntegerField()
    completado = models.BooleanField()