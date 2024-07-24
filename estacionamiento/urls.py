from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParkingLotViewSet, ReservationViewSet, SanctionViewSet

router = DefaultRouter()
router.register(r'parking-lots', ParkingLotViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'sanctions', SanctionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

