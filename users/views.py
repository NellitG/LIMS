from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]