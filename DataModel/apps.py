from django.apps import AppConfig


class AppUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AppUser'
class StationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Station'
class BookingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Booking'
