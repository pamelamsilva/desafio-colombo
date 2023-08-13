from rest_framework import viewsets

from colombo.product.models import Product
from colombo.product.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
