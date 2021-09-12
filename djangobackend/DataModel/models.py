from django.db import models

# Create your models here.
class AppUser(models.Model):
        user_id= models.AutoField(primary_key=True, blank=False, null=False)
        mobile_no = models.TextField(max_length=15, blank=False, null=False)
        password =  models.TextField(max_length=15, blank=False, null=False)
        fullname = models.TextField(max_length=30, blank=False, null=False)
        ev_brand = models.TextField(max_length=20, blank=False, null=False)
        ev_registration_no = models.TextField(max_length=15, blank=False, null=False)
        ev_type = models.TextField(max_length=15, blank=False, null=False)
        ev_port_type = models.TextField(max_length=15, blank=False, null=False)
        
class Station(models.Model):
        station_id= models.AutoField(primary_key=True, blank=False, null=False)
        station_name = models.TextField(max_length=30, blank=False, null=False)
        contact = models.TextField(max_length=15, blank=False, null=False)
        supported_port_type = models.TextField(max_length=50, blank=False, default='Type-A;Type-B;Type-C;Type-D;Type-E;Type-F')
        address = models.TextField(max_length=50, blank=False, null=False)
        state = models.TextField(max_length=20, blank=False, null=False)
        pincode = models.TextField(max_length=10, blank=False, null=False)
        latitude = models.TextField(max_length=50, blank=False, null=False)
        longitude = models.TextField(max_length=50, blank=False, null=False)

