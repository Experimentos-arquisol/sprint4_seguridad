from django.db import models

class ManejadorSolicitudes(models.Model):
    correo = models.EmailField(default='prueba@gmail.com')
    profesion = models.CharField(max_length=50)
    actividad_economica = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    ingresos = models.BigIntegerField()
    deudas = models.BigIntegerField()