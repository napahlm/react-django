from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Views

class RoomView(generics.ListAPIView):
    # Returns all room objects
    queryset = Room.objects.all()
    # Transforms into another format
    serializer_class = RoomSerializer
