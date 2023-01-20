from django.db import models
from user.models import MerchantBioData

# Create your models here

class ProductCategory(models.Model):
    product_category_name = models.CharField(max_length=255)

    def __str__(self):
        return  self.product_category_name

class ProductSubCategory(models.Model):
    product_sub_category_name = models.CharField(max_length=255)
    product_category =  models.ForeignKey(ProductCategory,on_delete=models.SET_DEFAULT,default=1)

    def __str__(self):
        return  self.product_sub_category_name


class Product(models.Model):
    product_category =  models.ForeignKey(ProductCategory,on_delete=models.SET_DEFAULT,default=1)
    product_sub_category =  models.ForeignKey(ProductSubCategory,on_delete=models.SET_DEFAULT,default=1)
    merchant =  models.ForeignKey(MerchantBioData,on_delete=models.SET_DEFAULT,default=1)
    product_name = models.CharField(max_length=255)
    product_description = models.CharField(max_length=255)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField() 
    product_image = models.ImageField(upload_to='product_images/',default='media/')


# class ReceiveOrderGroup(models.Model):

# class ReceiveOrderItems(models.Model):