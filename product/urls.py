from django.urls import path
from .views import allProducts

urlpatterns = [
    
    path ('AllProducts/',allProducts, name="AllProducts"),

  
]