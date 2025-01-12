# Imported files and packages
from django.db.models import Count
from rest_framework import generics, filters
from hg_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    Render all profiles in a paginated list.
    Profile creation is handled by django signals.
    Related to :model:`Profile`.
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
    Related to :model:`Profile`.
    """
    queryset = Profile.objects.annotate(
        reviews_made=Count('owner__review', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
