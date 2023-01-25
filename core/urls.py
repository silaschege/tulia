
from django.contrib import admin
from django.urls import path,include 

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('',include('home.urls'),name='home_urls'),
    # authentication system
    path('',include('django.contrib.auth.urls')),
    path('',include('product.urls'),name='product_urls'),
    path('cart',include('cart.urls'),name='cart_urls'),
    path('accounting',include('accounting.urls'),name='accounting_urls'),
    path('shipping',include('shipping.urls'),name='shipping_urls'),
    path('user',include('user.urls'),name='user_urls'),

]
