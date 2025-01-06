from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'updated_at', 'website',
            'product_image', 'image_alt',
        ]
