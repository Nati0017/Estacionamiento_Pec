from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status, permissions
from .models import ParkingLot, Reservation, Sanction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import ParkingLotSerializer, ReservationSerializer, SanctionSerializer
from .models import Person
from .serializers import PersonSerializer

class ParkingLotViewSet(viewsets.ModelViewSet):
    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class SanctionViewSet(viewsets.ModelViewSet):
    queryset = Sanction.objects.all()
    serializer_class = SanctionSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.AllowAny]

class PersonCreateView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)