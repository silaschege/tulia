
from django.contrib import admin
from django.urls import path,include 

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('',include('home.urls'),name='home_urls'),
    # authentication system
    path('',include('django.contrib.auth.urls')),
    path('',include('product.urls'),name='product_urls'),
    path('user',include('user.urls'),name='user_urls'),

]
