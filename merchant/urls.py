from django.urls import path
from .views import merchantStore

urlpatterns = [
   
    path ('MerchantStore/',merchantStore, name="MerchantStore"),
  
]