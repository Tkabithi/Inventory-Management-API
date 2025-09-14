from django.contrib.auth.models import User
from .serializers import UserSerializer, UserRegisterSerializer
from rest_framework import viewsets, permissions



# Register new user
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializer
        return UserSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]





