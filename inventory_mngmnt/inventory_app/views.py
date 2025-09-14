from django.shortcuts import render
from .models import InventoryItem, InventoryLog
from .serializers import InventoryItemSerializer,InventoryLogSerializer
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated



class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all().order_by('-date_added')
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner_id=self.request.user)

class InventoryLogViewSet(viewsets.ModelViewSet):
    queryset = InventoryLog.objects.all().order_by('-timestamp')
    serializer_class = InventoryLogSerializer
    permission_classes = [permissions.IsAuthenticated]

