from django.db import models
from django.utils import timezone


# Products
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    discount = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/')  # uploaded to MEDIA_ROOT/products
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    def get_discounted_price(self):
        """Calculate price after discount"""
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price
    
    def get_original_price(self):
        """Get original price before discount"""
        return self.price
    
    class Meta:
        ordering = ['-created_at']  # Newest first

# Reviews
class Review(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to='reviews/', blank=True, null=True)
    rating = models.IntegerField(default=5, choices=[(i, i) for i in range(1, 6)])  # 1-5 stars
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']  # Newest first

# Contact Messages
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']  # Newest first


# Create your models here.
