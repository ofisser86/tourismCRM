from django.db import models
from client.models import *
from tour.models import *


class Order(models.Model):
    class Meta(object):
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    ORDER_STATUS = (
        ('B', 'Booked'),
        ('PP', 'Partially Paid'),
        ('FP', 'Fully Paid'),
    )
    status = models.CharField(max_length=2, choices=ORDER_STATUS)
    client = models.ForeignKey(Client, default=None)
    tour = models.ForeignKey(Tour, default=None)
    # Count in view Total = tour_price * season_coefficient * count of tours
    count = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    order_total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


# Possibility addition tourist in Order. Family or friends of Client who ordered
class OrderTourist(models.Model):
    first_name = models.CharField(max_length=32, null=False, blank=False, verbose_name='First name')
    last_name = models.CharField(max_length=32, null=False, blank=False, verbose_name='Last name')
    birthday = models.DateField(blank=True, null=True, verbose_name='Date of birth')
    document_scan = models.ImageField(blank=True, null=True)
    client = models.ForeignKey(Client, default=None)
    order = models.ForeignKey(Order, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s %s (%s) ' % (self.first_name, self.last_name, self.client)


class DocumentOrderTourist(models.Model):
    order_tourist = models.ForeignKey(OrderTourist, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='order_tourist_doc/')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s " % self.id
