from django.db import models


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
