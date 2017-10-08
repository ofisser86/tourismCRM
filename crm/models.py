from django.db import models


# Create your models here.
class Email(models.Model):
    class Meta(object):
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

    client_email = models.ForeignKey('Client', on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True, verbose_name='Email')

    def __str__(self):
        return '%s' % self.client_email


class Phone(models.Model):
    class Meta(object):
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'

    client_phone = models.ForeignKey('Client', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=32, null=True, blank=True, verbose_name='Phone')

    def __str__(self):
        return '%s %s' % (self.client_phone, self.phone_number)


class PlusOne(models.Model):
    first_name = models.CharField(max_length=32, null=False, blank=False, verbose_name='First name' )
    last_name = models.CharField(max_length=32, null=False, blank=False, verbose_name='Last name' )
    birthday = models.DateField(blank=True, null=True, verbose_name='Date of birth')
    document_scan = models.ImageField(blank=True, null=True)
    client_plus_one = models.ForeignKey('Client')


class Client(models.Model):

    class Meta(object):
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    first_name = models.CharField(max_length=32, null=False, blank=False, verbose_name='First name')
    last_name = models.CharField(max_length=32, null=False, blank=False, verbose_name='Last name')
    middle_name = models.CharField(max_length=32, null=True, blank=True, verbose_name='Middle name')
    birthday = models.DateField(blank=True, null=True, verbose_name='Date of birth')
    document_scan = models.ImageField(blank=True, null=True)
    client_city = models.CharField(max_length=32, verbose_name='City')
    client_tour = models.ForeignKey('Tour')

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Country(models.Model):
    country_name = models.CharField(max_length=128, null=True, blank=True, verbose_name='Country')
    country_in_tour = models.ForeignKey('Tour')


class City(models.Model):
    city_name = models.CharField(max_length=128, null=True, blank=True, verbose_name='City')
    city_in_tour = models.ForeignKey('Tour')


class Hotel():
    hotel_name = models.CharField(max_length=256, null=False, blank=False, verbose_name='Hotel')
    hotel_star = models.IntegerField(default=1)
    # Hotel is full or available
    hotel_status = models.BooleanField()
    hotel_children_under_tree = models.BooleanField()
    hotel_pets_available = models.BooleanField()
    hotel_description = models.TextField(blank=True)
    hotel_in_tour = models.ForeignKey('Tour')


class TourSeason(models.Model):

    season = models.CharField(max_length=64, null=True, blank=True)
    # Some coefficient of season that on total tour price. Total = tour_price * season_coefficient * count of tours
    season_coefficient = models.IntegerField(default=1)
    season_in_tour = models.ForeignKey('Tour')


class Tour(models.Model):

    class Meta(object):
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'
    # Duration will be counting in view with using timedelta
    tour_start_date = models.DateField()
    tour_end_date = models.DateField()
    tour_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # Count of tours
    tour_nmb = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


class Order(models.Model):
    class Meta(object):
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'

    ORDER_STATUS = (
        ('B', 'Booked'),
        ('PP', 'Partially Payd'),
        ('FP', 'Fully Paid'),
    )
    status = models.CharField(max_length=1, choices=ORDER_STATUS)
    purchase_client = models.ForeignKey(Client)
    purchase_tour = models.ForeignKey(Tour)
    # Count in view Total = tour_price * season_coefficient * count of tours
    order_total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    tour_count = models.IntegerField(default=1)
