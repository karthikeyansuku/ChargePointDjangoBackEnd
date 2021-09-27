from django.contrib import admin
from .models import AppUser, Booking,Station
# Register your models here.
admin.site.register(Station)
admin.site.register(AppUser)
admin.site.register(Booking)