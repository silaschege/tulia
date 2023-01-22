from django.shortcuts import render
from product.models import Product

# Create your views here.

def home (request):
    product = Product.objects.all()
    return render(request,'homeTemplate/home.html',{'product':product})
   