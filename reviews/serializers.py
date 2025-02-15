# Imported files and packages
from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Review
from products.models import Product


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializes data for Review model,allowing JSON to be rendered.
    Related to :model:`Review`.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_image.url')

    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all())
    product_id = serializers.ReadOnlyField(source='product.id')
    product_name = serializers.ReadOnlyField(source='product.name')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Review
        fields = [
            'id', 'owner', 'profile_image', 'content', 'product_id',
            'product_name', 'rating', 'created_at', 'updated_at', 'is_owner',
            'product',
        ]
