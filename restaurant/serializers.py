from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from .models import MenuItem, Booking


class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class bookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']