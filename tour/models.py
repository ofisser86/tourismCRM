from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=128, null=True, blank=True, verbose_name='Country')

    def __str__(self):
        return '%s' % self.country_name


class CountryImage(models.Model):
    country = models.ForeignKey(Country, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='country_img/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s " % self.id


class City(models.Model):
    city_name = models.CharField(max_length=128, null=True, blank=True, verbose_name='City')

    def __str__(self):
        return '%s' % self.city_name


class CityImage(models.Model):
    city = models.ForeignKey(City, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='city_img/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' % self.id


class Hotel(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, verbose_name='Hotel')
    star = models.IntegerField(default=1)
    # Hotel is full or available
    status = models.BooleanField(default=True, verbose_name='Status is available if checked')
    children_under_tree = models.BooleanField()
    pets_available = models.BooleanField()
    description = models.TextField(blank=True)

    def __str__(self):
        return '%s' % self.name


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='hotel_img/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s " % self.id

    class Meta:
        verbose_name = 'Hotel Photo'
        verbose_name_plural = 'Hotels photos'


class TourSeason(models.Model):
    season = models.CharField(max_length=64, null=True, blank=True)
    # Some coefficient of season that in total tour price. Total = tour_price * season_coefficient * count of tours
    season_coefficient = models.IntegerField(default=1)
    season_start_date = models.DateField(default=None)
    season_end_date = models.DateField(default=None)


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
