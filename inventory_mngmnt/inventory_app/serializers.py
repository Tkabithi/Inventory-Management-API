from rest_framework import serializers
from django.contrib.auth.models import User
from .models import InventoryItem, InventoryLog




class InventoryItemSerializer(serializers.ModelSerializer):
    owner_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = InventoryItem
        fields = [
            'id',
            'name',
            'description',
            'quantity',
            'price',
            'category',
            'date_added',
            'last_updated',
            'owner_id',            
        ]

class InventoryLogSerializer(serializers.ModelSerializer):
    item = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = InventoryLog
        fields = ["id", "item","user","action","old_quantity","new_quantity","timestamp"]
