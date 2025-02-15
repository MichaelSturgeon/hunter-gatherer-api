# Imported files and packages
from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializes data for Product model,allowing JSON to be rendered.
    Related to :model:`Product`.
    """
    reviews_count = serializers.ReadOnlyField()
    updated_at = serializers.SerializerMethodField()

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'updated_at', 'website',
            'product_image', 'image_alt', 'reviews_count',
        ]
