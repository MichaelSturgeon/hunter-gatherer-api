# Imported files and packages
from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """
    Stores a instence of a review entry.
    Related to :model:`auth.User`.
    """
    # Review rating variables
    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=800, blank=False)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES, default=1)

    # Returns instances of reviews in reverse order
    class Meta:
        ordering = ['-created_at']

    # Return an easily readable string of review owner
    def __str__(self):
        return f"{self.owner} | {self.product} | {self.rating}"
