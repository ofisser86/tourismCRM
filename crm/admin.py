from django.contrib import admin
from .models import  Client, Email, Phone
# Register your models here.

class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0

class ClientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Client._meta.fields]
    # phone = Phone.objects.filter()
    # print(phone)
    # list_display = ('first_name', 'last_name', 'phone')
    inlines = [PhoneInline]

    class Meta(object):
        model = Client


admin.site.register(Client, ClientAdmin)
admin.site.register(Email)
admin.site.register(Phone)