from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles. Profile creation is handled by django signals.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
