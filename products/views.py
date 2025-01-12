# Imported files and packages
from django.db.models import Count
from rest_framework import generics, filters
from .models import Product
from .serializers import ProductSerializer


class ProductList(generics.ListAPIView):
    """
    Render all products in a paginated list.
    Related to :model:`Product`.
    """
    queryset = Product.objects.annotate(
        reviews_count=Count('review', distinct=True)
    ).order_by('-updated_at')
    serializer_class = ProductSerializer

    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'name',
        'price',
        'reviews_count',
    ]


class ProductDetail(generics.RetrieveAPIView):
    """
    Retrieve a product given a valid id.
    Related to :model:`Product`.
    """
    queryset = Product.objects.annotate(
        reviews_count=Count('review', distinct=True)
    ).order_by('-updated_at')
    serializer_class = ProductSerializer
