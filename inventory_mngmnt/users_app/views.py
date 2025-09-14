from django.contrib.auth.models import User
from .serializers import UserSerializer, UserRegisterSerializer
from rest_framework import viewsets, permissions

# Register new user
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializer
        return UserSerializer





