from sre_constants import CATEGORY
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

LOCATION_CHOICES = [
    ('Location1', 'L1'),
    ('Location2', 'L2'),
    ('Null', 'Null'),
]


class Info(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    # Use a RegexValidator to enforce a specific phone number format
    phone_regex = RegexValidator(
        regex=r'^\d{11}$',  # Modify the regex pattern to match your desired format
        message="Phone number must be exactly 10 digits without spaces or dashes and must be exactly 11 digits"
    )
    
    phone_no = models.CharField(
        max_length=17,
        validators=[phone_regex]
    )

    hostel = models.CharField(max_length=250)
    location = models.CharField(
        max_length=9,
        choices=LOCATION_CHOICES,
        default='Null',
        null=True
    )

    comment = models.CharField(max_length=400)