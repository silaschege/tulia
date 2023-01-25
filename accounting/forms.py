from django import forms
from django.forms import ModelForm
from .models import userShippingPayment

class userShippingPaymentFrom(ModelForm):
    class Meta:
        model = userShippingPayment
        fields = ('payment_on_delivery','payment_via_mpesa','payment_via_credit', )

        labels = {  
                    'payment_on_delivery':'payment_on_delivery',
                    'payment_via_mpesa':'payment_via_mpesa',
                    'payment_via_credit':'payment_via_credit',
                     }
        widget = {  }