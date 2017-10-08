from django.contrib import admin

from crm.models.tour import PlusOne
from .models import *
# Register your models here.


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0


class EmailInline(admin.TabularInline):
    model = Email
    extra = 0


class PlusOneInline(admin.TabularInline):
    model = PlusOne
    extra = 0


class ClientInline(admin.TabularInline):
    model = Client
    extra = 0


class ClientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Client._meta.fields]
    inlines = [PhoneInline, EmailInline, PlusOneInline]

    class Meta(object):
        model = Client

class TourAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tour._meta.fields]
    inlines = [ClientInline, PlusOneInline]


admin.site.register(Client, ClientAdmin)
admin.site.register(Email)
admin.site.register(Phone)
admin.site.register(Tour, TourAdmin)
admin.site.register(Order)
admin.site.register(Hotel)
admin.site.register(City)
admin.site.register(TourSeason)
admin.site.register(Country)