from django.contrib import admin

from django.contrib import admin
from .models import ParkingLot, Reservation, Sanction

class ParkingLotAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'total_espacios', 'espacios_disponibles', 'compartido')

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'estacionamiento', 'fecha_reserva', 'hora_inicio', 'hora_fin', 'estado')

class SanctionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo', 'fecha', 'duracion')

admin.site.register(ParkingLot, ParkingLotAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Sanction, SanctionAdmin)

# Register your models here.
