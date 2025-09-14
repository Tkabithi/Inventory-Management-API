from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet   # make sure this is imported

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')  # viewset is passed here

urlpatterns = [
    path('', include(router.urls)),
]

