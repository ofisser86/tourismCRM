from django.contrib import admin
from .models import *


# Register your models here.
class TourAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tour._meta.fields]


admin.site.register(Tour, TourAdmin)
admin.site.register(Hotel)
admin.site.register(City)
admin.site.register(TourSeason)
admin.site.register(Country)
