from django.contrib.auth.models import User, Group 
from rest_framework import serializers
from DataModel.models import AppUser, Station, Booking


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']
        
class AppUserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = AppUser
        fields=['user_id','mobile_no', 'password', 'fullname', 'ev_brand', 'ev_registration_no', 'ev_type', 'ev_port_type']

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['station_id','station_name', 'contact', 'supported_port_type', 'address', 'state', 'pincode', 'latitude', 'longitude']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['booking_id','station_id', 'user_id', 'date', 'time', 'status']
