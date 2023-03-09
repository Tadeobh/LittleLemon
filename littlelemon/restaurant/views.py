from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView

from .models import Menu, Booking
from .serializers import MenuSerializer

# Create your views here.
class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer