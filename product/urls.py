from django.urls import path
from .views import (
                    allProducts,
                    addProductCategory,
                    addProductSubCategory,
                    addProduct,
                    addProduct_productSubCategoryChained,
                    merchantStore,
                    allProductCategory,
                    allProductSubCategory
                    )

urlpatterns = [
    
    path (' ',allProducts, name="AllProducts"),
    path ('AddProductCategory/',addProductCategory, name="AddProductCategory"),
    path ('AllProductCategory/',allProductCategory, name="AllProductCategory"),
    path ('AddProductSubCategory/',addProductSubCategory, name="AddProductSubCategory"),
    path ('AllProductSubCategory/',allProductSubCategory, name="AllProductSubCategory"),
    path ('AddProduct/',addProduct, name="AddProduct"),
    path ('AddProduct_productSubCategoryChained/',addProduct_productSubCategoryChained, name="AddProduct_productSubCategoryChained"),
    path ('MerchantStore/',merchantStore, name="MerchantStore"),

  
]