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

from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
