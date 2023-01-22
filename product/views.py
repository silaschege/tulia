from django.shortcuts import render,redirect
from .forms import AddProductCategoryForm,AddProductSubCategoryForm,AddProductForm
from .models import ProductCategory,ProductSubCategory,Product
import json 
from django.http import JsonResponse
from user.models import MerchantEmployees,MerchantBioData

# Create your views here.
def allProducts (request):
    product = Product.objects.all()
    return render(request,'generalProductTemplate/allProducts.html',{'product':product})

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
            product=form.save(commit=False)
            user = request.user
            merchant_id = MerchantEmployees.objects.filter(employee=user).values('merchant_id')
            print(merchant_id)
            for i in merchant_id:
                merchant = MerchantBioData.objects.get(pk = i['merchant_id'])
                print(merchant)
                product.merchant = merchant
                product.save()
                return redirect('MerchantStore')

    return render(request,'merchantProductTemplate/addProduct.html',{'form':form})

# this is a fuction for the chained dropdown ProductSubCategory
def addProduct_productSubCategoryChained(request):
    data = json.loads(request.body)
    category_id = data['id']
    product_sub_category =ProductSubCategory.objects.filter(product_category=category_id)
    return JsonResponse(list(product_sub_category.values('id','product_sub_category_name')),safe=False)

def merchantStore (request):
    User = request.user
    merchant = MerchantEmployees.objects.filter(employee=User).values('merchant_id')
    products=[]
    for i in merchant:
        productfilter = Product.objects.filter(merchant=i['merchant_id'])
        products.append(productfilter)
    return render(request,'merchantProductTemplate/merchantStore.html',{'products':products})