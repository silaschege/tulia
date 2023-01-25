from django.urls import path
from .views import addUserShippingLocation,userShippingReceipt

urlpatterns = [
    path ('AddUserShippingLocation/',addUserShippingLocation, name="AddUserShippingLocation"),
    path ('UserShippingReceipt/',userShippingReceipt, name="UserShippingReceipt"),
]