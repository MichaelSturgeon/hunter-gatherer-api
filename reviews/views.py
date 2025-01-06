from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer


class ReviewList(generics.ListAPIView):
    """
    List all reviews.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

