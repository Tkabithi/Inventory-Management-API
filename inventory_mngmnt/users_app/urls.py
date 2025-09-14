from django.urls import path
from .views import UserRegisterView, UserListView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('list/', UserListView.as_view(), name='user-list'),
]
