from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserRegisterSerializer
from rest_framework import generics

# Register new user
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

# List all users
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



