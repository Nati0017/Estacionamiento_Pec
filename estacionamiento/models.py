
# models.py
from django.db import models
from django.contrib.auth.models import User

class ParkingLot(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    total_espacios = models.IntegerField()
    espacios_disponibles = models.IntegerField()
    compartido = models.BooleanField(default=False)

class Reservation(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estacionamiento = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    estado = models.CharField(max_length=50, default='confirmada')

class Sanction(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    duracion = models.IntegerField()  # Duración en días

