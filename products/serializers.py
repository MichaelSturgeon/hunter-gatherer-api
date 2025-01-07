from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    reviews_count = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'updated_at', 'website',
            'product_image', 'image_alt', 'reviews_count',
        ]
