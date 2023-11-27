# Create your views here.
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from restaurant.models import Booking, MenuItem
from restaurant.serializers import bookingSerializer, MenuItemSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    permission_classes = [permissions.IsAuthenticated]

class MenuItemsView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer