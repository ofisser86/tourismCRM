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


class Client(models.Model):

    class Meta(object):
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    first_name = models.CharField(max_length=32, null=False, blank=False, verbose_name='First name')
    last_name = models.CharField(max_length=32, null=False, blank=False, verbose_name='Last name')
    middle_name = models.CharField(max_length=32, null=True, blank=True, verbose_name='Middle name')
    birthday = models.DateField(blank=True, null=True, verbose_name='Date of birth')
    document_scan = models.ImageField(blank=True, null=True)
    client_tour = models.ForeignKey('Tour', default=None)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)