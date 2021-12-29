from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RoomSerializer, CreateRoomSerializer
from .models import Room
from rest_framework.views import APIView
from rest_framework.response import Response

# Views

class RoomView(generics.ListAPIView):
    # Returns all room objects
    queryset = Room.objects.all()
    # Transforms into another format
    serializer_class = RoomSerializer

class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer

    def post(self, request, format=None):

        # Create a unique session key
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        # Create a room from valid serializer data
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key

            # Check if the host already has a session
            queryset = Room.objects.filter(host=host)
            if queryset.exists():
                # Update existing room session
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                # Force update
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
            else:
                # Create room
                room = Room(host=host, guest_can_pause=guest_can_pause,
                            votes_to_skip=votes_to_skip)
                room.save() # Creates the room
                return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)

            # Get room diagnostics and return room
        return Response({'Bad Request: Invalid data ...'}, status=status.HTTP_400_BAD_REQUEST) # Contains the room
