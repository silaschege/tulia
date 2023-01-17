from django.shortcuts import render

# Create your views here.
def allProducts (request):
    return render(request,'productTemplate/allProducts.html',{})