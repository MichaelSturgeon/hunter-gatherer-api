from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    description = models.CharField(max_length=800, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    updated_at = models.DateTimeField(auto_now=True)
    website = models.URLField(max_length=300, blank=False)
    product_image = models.ImageField(
        upload_to='images/', default='../default_post_w4egx3'
    )
    image_alt = models.CharField(max_length=300, blank=False)

    # Returns instances of products in reverse order
    class Meta:
        ordering = ['-updated_at']

    # Return an easily readable string of product name
    def __str__(self):
        return f"{self.name}"
