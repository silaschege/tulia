from django.contrib import admin
from .models import userShippingLocation,userShippingNumber,userShippingItems

# Register your models here.
admin.site.register(userShippingLocation)
admin.site.register(userShippingNumber)
admin.site.register(userShippingItems)
