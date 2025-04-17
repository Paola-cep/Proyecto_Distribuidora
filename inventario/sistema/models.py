from django.db import models

class Compra(models.Model):
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    total = models.FloatField()
    fecha = models.DateTimeField()

class Venta(models.Model):
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    total = models.FloatField()
    fecha = models.DateTimeField()

