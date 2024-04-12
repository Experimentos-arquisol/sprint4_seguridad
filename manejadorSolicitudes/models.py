from django.db import models

class ManejadorSolicitudes(models.Model):
    profesion = models.CharField(max_length=50)
    actividad_economica = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    ingresos = models.BigIntegerField()
    deudas = models.BigIntegerField()