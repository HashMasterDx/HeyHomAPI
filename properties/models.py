from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models


# Property model
class Property(models.Model):
    HOUSE = 'House'
    APARTMENT = 'Apartment'
    TOWNHOUSE = 'Townhouse'

    PROPERTY_TYPES = (
        (HOUSE, 'House'),
        (APARTMENT, 'Apartment'),
        (TOWNHOUSE, 'Townhouse'),
    )

    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(validators=[MinValueValidator(0)], max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPES)
    bedrooms = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])
    bathrooms = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])
    square_feet = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999999)])
    available = models.BooleanField(default=True)


# User model
class CustomUser(AbstractUser):
    bio = models.CharField(max_length=255, blank=True)
