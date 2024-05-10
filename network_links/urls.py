from rest_framework.routers import DefaultRouter

from network_links.apps import NetworkLinksConfig
from network_links.views import SupplierViewSet

app_name = NetworkLinksConfig.name

router = DefaultRouter()
router.register(r'supplier', SupplierViewSet, basename='supplier')

urlpatterns = [
] + router.urls
