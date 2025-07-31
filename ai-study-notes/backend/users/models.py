from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User model with additional fields."""
    
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=500, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Use email as the username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # No additional required fields since email is the username
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
