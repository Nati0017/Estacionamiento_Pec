from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from estacionamiento.views import ParkingLotViewSet, ReservationViewSet, SanctionViewSet

router = DefaultRouter()
router.register(r'parking-lots', ParkingLotViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'sanctions', SanctionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]