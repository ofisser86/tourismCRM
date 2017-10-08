from django.db import models
from .client import *
from .tour import *


class Order(models.Model):
    class Meta(object):
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    ORDER_STATUS = (
        ('B', 'Booked'),
        ('PP', 'Partially Paid'),
        ('FP', 'Fully Paid'),
    )
    status = models.CharField(max_length=1, choices=ORDER_STATUS)
    order_client = models.ForeignKey(Client)
    order_tour = models.ForeignKey(Tour)
    # Count in view Total = tour_price * season_coefficient * count of tours
    order_total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    tour_count = models.IntegerField(default=1)