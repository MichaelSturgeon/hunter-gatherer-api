# Imported files and packages
from rest_framework import generics, filters
from hg_api.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer


class ReviewList(generics.ListCreateAPIView):
    """
    Renders all reviews in a paginated list.
    Related to :model:`Review`.
    """
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer

    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'owner__username',
        'rating',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a review given an id,
    and update a review given an authorized user.
    Related to :model:`Review`.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]
