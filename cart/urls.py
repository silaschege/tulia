from django.urls import path
from .views import addCart,userCart,userCartRemove

urlpatterns = [
    path ('AddCart/<id>',addCart, name="AddCart"),
    path ('UserCart/',userCart, name="UserCart"),
    path ('UserCartRemove/<id>',userCartRemove, name="UserCartRemove"),
]