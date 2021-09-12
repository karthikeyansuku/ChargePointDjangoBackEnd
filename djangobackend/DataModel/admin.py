from django.contrib import admin
from .models import AppUser,Station
# Register your models here.
admin.site.register(Station)
admin.site.register(AppUser)