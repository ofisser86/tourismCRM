from django.db import models


# Create your models here.
class Email(models.Model):
    class Meta(object):
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

    email = models.EmailField(null=True, blank=True, verbose_name='Email')

    def __str__(self):
        return '%s' % self.email


class Phone(models.Model):
    class Meta(object):
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'

    phone_number = models.CharField(max_length=32, null=True, blank=True, verbose_name='Phone')

    def __str__(self):
        return '%s' % self.phone_number


class Client(models.Model):

    class Meta(object):
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    first_name = models.CharField(max_length=32, null=False, blank=False, verbose_name='First name' )
    last_name = models.CharField(max_length=32, null=False, blank=False, verbose_name='Last name')
    middle_name = models.CharField(max_length=32, null=False, blank=False, verbose_name='Middle name')
    client_city = models.CharField(max_length=32, verbose_name='City')
    client_phone = models.ForeignKey('Phone', on_delete=models.CASCADE)
    client_email = models.ForeignKey('Email', on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s %s, %s, %s' % (self.first_name, self.last_name, self.client_city, self.client_email.email, self.client_phone.phone_number)


# class Tour(models.Model):
#     class Meta(object):
#         verbose_name = 'Tour'
#         verbose_name_plural = 'Tours'
#
#     tour_country = models.CharField(max_length=32)
#     tour_city = models.CharField(max_length=32)
#     tour_hotel = models.CharField(max_length=256)
#     tour_start_date = models.DateField()
#     tour_end_date = models.DateField()
#     tour_price = models.IntegerField()
#
#
# class Purchase(models.Model):
#     class Meta(object):
#         verbose_name = 'Purchase'
#         verbose_name_plural = 'Purchases'
#
#     PURCHASE_STATUS = (
#         ('B', 'Booked'),
#         ('PP', 'Partially Payd'),
#         ('FP', 'Fully Paid'),
#     )
#     status = models.CharField(max_length=1, choices=PURCHASE_STATUS)
#     purchase_client = models.ForeignKey(Client)
#     purchase_tour = models.ForeignKey(Tour)
#     tour_count = models.IntegerField()
