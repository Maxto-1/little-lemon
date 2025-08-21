from django.shortcuts import render
from rest_framework import generics
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from .models import Specialite

def index(request):
    specialites = Specialite.objects.all()
    return render(request, 'index.html', {'specialites': specialites})

def menu(request):
    return render(request, 'menu.html')

def reservation(request):
    return render(request, 'reservation.html')

class MenuAPIView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingAPIView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer