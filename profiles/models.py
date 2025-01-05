from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    profile_image = models.ImageField(
        upload_to='images/', default='../default_profile_fy5gbu'
    )

    # Returns instances of profiles in reverse order
    class Meta:
        ordering = ['-created_at']

    # Return an easily readable string of profile users
    def __str__(self):
        return f"{self.owner}'s profile"


# Defines the create_profile function
def create_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(owner=instance)


# Listens for the post_save signal coming from the User model
# when the connect function is called
post_save.connect(create_profile, sender=User)
