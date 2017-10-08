from django.contrib import admin
from .models import *
# Register your models here.


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0


class EmailInline(admin.TabularInline):
    model = Email
    extra = 0

class ClientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Client._meta.fields]
    inlines = [PhoneInline, EmailInline]

    class Meta(object):
        model = Client


admin.site.register(Client, ClientAdmin)
admin.site.register(Email)
admin.site.register(Phone)
admin.site.register(Tour)
admin.site.register(Order)