from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class userShippingPayment(models.Model):
    user =  models.ForeignKey(User,on_delete=models.SET_DEFAULT,default=1)
    payment_on_delivery = models.BooleanField()
    payment_via_mpesa = models.BooleanField()
    payment_via_credit = models.BooleanField()




