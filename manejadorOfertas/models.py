from django.db import models

class Oferta(models.Model):
    correo = models.EmailField(default='correo@default.com')
    tipo_oferta = models.CharField(max_length=50)
