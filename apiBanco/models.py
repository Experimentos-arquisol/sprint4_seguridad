from django.db import models

class ApiBanco(models.Model):


    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=10)
    contrasenia = models.CharField(max_length=10)



# Create your models here.
