from django.db import models
from django.db.models.functions import Now

from valuations.constants import ROLL_TYPE_CHOICES, CITY_CHOICES


class Valuation(models.Model):
    last_modified = models.DateTimeField(auto_now=True, db_default=Now())
    city = models.CharField(max_length=50, choices=CITY_CHOICES, default=CITY_CHOICES["durban"], db_default=CITY_CHOICES["durban"])
    roll_type = models.CharField(max_length=50, choices=ROLL_TYPE_CHOICES)
    rate_number = models.CharField(max_length=200)
    legal_description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    first_owner = models.CharField(max_length=200)
    use_code = models.CharField(max_length=200)
    rating_category = models.CharField(max_length=200)
    market_value = models.DecimalField(decimal_places=3, max_digits=40)
    registered_extent = models.DecimalField(decimal_places=3, max_digits=40)
