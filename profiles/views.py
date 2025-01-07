from django.db.models import Count
from rest_framework import generics, filters
from hg_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles. Profile creation is handled by django signals.
    """
    queryset = Profile.objects.annotate(
        reviews_made=Count('owner__review', distinct=True)
    ).order_by('-created_at')

    serializer_class = ProfileSerializer

    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'owner__username',
        'reviews_made',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve a profile given an id,
    and update a profile given an authorized user.
    """
    queryset = Profile.objects.annotate(
        reviews_made=Count('owner__review', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
