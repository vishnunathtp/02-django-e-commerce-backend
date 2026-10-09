from rest_framework import viewsets, filters
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'sku']
    ordering_fields = ['price', 'created_at']
