from DataModel.views import AppUserViewSet, StationViewSet, BookingViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('AppUsers', AppUserViewSet)
router.register('Stations', StationViewSet)
router.register('Bookings', BookingViewSet)