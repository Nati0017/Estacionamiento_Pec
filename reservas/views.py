from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import ParkingLot, Reservation, Sanction
from .models serializers import ParkingLotSerializer, ReservationSerializer, SanctionSerializer

# Create your views here.
# views.py

class ParkingLotViewSet(viewsets.ModelViewSet):
    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class SanctionViewSet(viewsets.ModelViewSet):
    queryset = Sanction.objects.all()
    serializer_class = SanctionSerializer
