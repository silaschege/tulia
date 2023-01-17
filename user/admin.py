from django.contrib import admin
from .models import UserAccount,MerchantBioData,MerchantEmployees
# Register your models here.
admin.site.register(UserAccount)
admin.site.register(MerchantBioData)
admin.site.register(MerchantEmployees)
