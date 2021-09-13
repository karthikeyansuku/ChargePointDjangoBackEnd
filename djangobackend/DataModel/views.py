from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework_swagger.views import get_swagger_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
import json
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User, Group
from DataModel.serializers import AppUserSerializer, StationSerializer, BookingSerializer, UserSerializer
from DataModel.models import AppUser, Station, Booking


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class AppUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows app users registerred to be viewed or edited.
    """
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    permission_classes = [permissions.IsAuthenticated]

class StationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows app users registerred to be viewed or edited.
    """
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows app users registerred to be viewed or edited.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

schema_view = get_swagger_view(title='ChargePoint APIs')
