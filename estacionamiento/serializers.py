from rest_framework import serializers
from .models import ParkingLot, Reservation, Sanction

class ParkingLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingLot
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class SanctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sanction
        fields = '__all__'