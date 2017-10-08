from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=128, null=True, blank=True, verbose_name='Country')

    def __str__(self):
        return '%s' % self.country_name


class City(models.Model):
    city_name = models.CharField(max_length=128, null=True, blank=True, verbose_name='City')

    def __str__(self):
        return '%s' % self.city_name

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=256, null=False, blank=False, verbose_name='Hotel')
    hotel_star = models.IntegerField(default=1)
    # Hotel is full or available
    hotel_status = models.BooleanField(default=True, verbose_name='Status is available')
    hotel_children_under_tree = models.BooleanField()
    hotel_pets_available = models.BooleanField()
    hotel_photo = models.ImageField(blank=True, null=True)
    hotel_description = models.TextField(blank=True)

    def __str__(self):
        return '%s' % self.hotel_name


class TourSeason(models.Model):

    season = models.CharField(max_length=64, null=True, blank=True)
    # Some coefficient of season that in total tour price. Total = tour_price * season_coefficient * count of tours
    season_coefficient = models.IntegerField(default=1)
    season_start_date = models.DateField(default=None)
    season_end_date = models.DateField(default=None)


class PlusOne(models.Model):
    first_name = models.CharField(max_length=32, null=False, blank=False, verbose_name='First name' )
    last_name = models.CharField(max_length=32, null=False, blank=False, verbose_name='Last name' )
    birthday = models.DateField(blank=True, null=True, verbose_name='Date of birth')
    document_scan = models.ImageField(blank=True, null=True)
    client_plus_one = models.ForeignKey('Client', default=None)
    plus_one_in_tour = models.ForeignKey('Tour', default=None)

    def __str__(self):
        return '%s %s (%s) ' % (self.first_name, self.last_name, self.client_plus_one)


class Tour(models.Model):

    class Meta(object):
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'
    # Duration will be counting in view with using timedelta (if not need to count in Admin)
    title = models.CharField(max_length=256, null=True, blank=True, verbose_name='Tour')
    tour_start_date = models.DateField()
    tour_end_date = models.DateField()
    country = models.OneToOneField(Country, default=None)
    city = models.OneToOneField(City, default=None)
    hotel = models.OneToOneField(Hotel, default=None)
    season = models.OneToOneField(TourSeason, default=None)
    tour_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
