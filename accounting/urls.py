from django.urls import path
from .views import userShippingPayment

urlpatterns = [
    path ('UserShippingPayment/',userShippingPayment, name="UserShippingPayment"),
]