from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from network_links.models import Supplier
from network_links.permissions import IsActive
from network_links.serializers import SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsActive,]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('city',)
