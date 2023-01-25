from django.contrib import admin
from .models import ProductCategory,ProductSubCategory,Product
# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(ProductSubCategory)
admin.site.register(Product)
