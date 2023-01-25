from django.db import models
from user.models import UserAccount
from product.models import Product

# Create your models here.
class userShippingLocation(models.Model):
    user =  models.ForeignKey(UserAccount,on_delete=models.SET_DEFAULT,default=1)
    country = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    estate = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    major_landmark = models.CharField(max_length=255)

class userShippingNumber(models.Model):
    user =  models.ForeignKey(UserAccount,on_delete=models.SET_DEFAULT,default=1)
    total = models.IntegerField()
    prepare = models.BooleanField(default=False)
    on_transit =  models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)



class userShippingItems(models.Model):
    shipping_number =  models.ForeignKey(userShippingNumber,on_delete=models.SET_DEFAULT,default=1)
    product =  models.ForeignKey(Product,on_delete=models.SET_DEFAULT,default=1)
    quantity = models.IntegerField()
    

