from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_image = serializers.ReadOnlyField(source='owner.profile.profile_image.url')
    product = serializers.ReadOnlyField(source='product.id')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Review
        fields = [
            'id', 'owner', 'profile_image', 'content', 'product',
            'rating', 'created_at', 'updated_at', 'is_owner',
        ]
