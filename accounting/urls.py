from django.urls import path
from .views import userShippingPayment,userShippingReceipt

urlpatterns = [
    path ('UserShippingPayment/',userShippingPayment, name="UserShippingPayment"),
    path ('UserShippingReceipt/',userShippingReceipt, name="UserShippingReceipt"),
]