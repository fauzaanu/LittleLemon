# Create your views here.
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from restaurant.models import Booking, Menu
from restaurant.serializers import bookingSerializer, menuSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    permission_classes = [permissions.IsAuthenticated]

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer