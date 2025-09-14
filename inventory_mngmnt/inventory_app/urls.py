from rest_framework.routers import DefaultRouter
from .views import InventoryItemViewSet, InventoryLogViewSet

router = DefaultRouter()
router.register(r'items', InventoryItemViewSet, basename='inventoryitem')
router.register(r'logs', InventoryLogViewSet, basename='inventorylog')

urlpatterns = router.urls
