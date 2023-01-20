from django.shortcuts import render,redirect
from .forms import AddProductCategoryForm,AddProductSubCategoryForm,AddProductForm
from .models import ProductCategory,ProductSubCategory
import json 
from django.http import JsonResponse

# Create your views here.
def allProducts (request):
    return render(request,'generalProductTemplate/allProducts.html',{})

def addProductCategory (request):
    form = AddProductCategoryForm()
    if request.method == 'POST':
        form = AddProductCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AllProductCategory')
            
    return render(request,'adminProductsTemplate/addProductCategory.html',{'form':form})

def allProductCategory (request):
    category = ProductCategory.objects.all()
    return render (request,'adminProductsTemplate/allProductCategories.html',{'category':category,})

def addProductSubCategory (request):
    form = AddProductSubCategoryForm()
    if request.method == 'POST':
        form = AddProductSubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AllProductSubCategory')

    return render(request,'adminProductsTemplate/addProductSubCategory.html',{'form':form})

def allProductSubCategory(request):
    sub_category = ProductSubCategory.objects.all()
    return render(request,'adminProductsTemplate/allProductSubCategories.html',{'sub_category':sub_category,})

def addProduct (request):
    form = AddProductForm()
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('MerchantStore')
    return render(request,'merchantProductTemplate/addProduct.html',{'form':form})

# this is a fuction for the chained dropdown ProductSubCategory
def addProduct_productSubCategoryChained(request):
    data = json.loads(request.body)
    category_id = data['id']
    print(category_id)
    product_sub_category =ProductSubCategory.objects.filter(product_category=category_id)
    return JsonResponse(list(product_sub_category.values('id','product_sub_category_name')),safe=False)

def merchantStore (request):
    
    return render(request,'merchantProductTemplate/merchantStore.html',{})