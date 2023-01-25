from django.db import models
from user.models import UserAccount
from product.models import Product

# Create your models here.
class UserCart(models.Model):
    user =  models.ForeignKey(UserAccount,on_delete=models.SET_DEFAULT,default=1)
    product =  models.ForeignKey(Product,on_delete=models.SET_DEFAULT,default=1)
    quantity = models.IntegerField()
