from django.urls import path
from .views import UserRegisterView, UserListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('',UserListView.as_view(),name='user-home'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('list/', UserListView.as_view(), name='user-list'),

    path('login/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
]
