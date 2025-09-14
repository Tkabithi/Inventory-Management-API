from django.db import models
from django.contrib.auth.models import User

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inventory_items')

    def __str__(self):
        return f"{self.name} (Qty: {self.quantity})"
    
class InventoryLog(models.Model):
    ACTION_CHOICES = [
        ('ADD', 'Added'),
        ('UPDATE', 'Updated'),
        ('DELETE', 'Deleted'),
    ]
    
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE,related_name='logs')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'logs')
    action = models. CharField(max_length=50, choices=ACTION_CHOICES)
    old_quantity = models.PositiveIntegerField(null=True, blank=True)
    new_quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.action} {self.item.name} by {self.user.username} at {self.timestamp}"



