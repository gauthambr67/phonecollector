from django.contrib import admin
from .models import Phone, Charging, Accessory

# Register your models here.
admin.site.register(Phone)
admin.site.register(Charging)
admin.site.register(Accessory)