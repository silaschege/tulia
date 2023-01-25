from django.shortcuts import render,redirect
from .models import UserCart
from product.models import Product
from django.http import HttpResponseRedirect

# Create your views here.
def addCart(request,id):
   loginUser = request.user
   product_get = Product.objects.get(pk=id)
   exist=UserCart.objects.filter(user = loginUser ,product = id).count()
   
   print(loginUser)
   if request.user.is_anonymous == True:
       return redirect('Login')

   if exist >=1:
      cart=UserCart.objects.filter(user = loginUser ,product = id)
      cart_updated = cart.quantity+1
      
      UserCart.objects.filter(user = loginUser ,product = product_get).update(quantity=cart_updated)
   elif exist <= 1:
      
      UserCart.objects.create(user = loginUser ,product = product_get,quantity=1 )
      
   return render(request,'generalCart/cart.html',{})

def userCartRemove(request,id):
    cart=UserCart.objects.get(product=id,user=request.user)
    quant = cart.quantity
    if quant>1:
        quantityupdated = cart.quantity-1
        UserCart.objects.filter(product=id,user=request.user).update(quantity=quantityupdated)
    elif quant <=1:
        cart.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def userCart(request):
   loginUser = request.user
   cart=UserCart.objects.filter(user=loginUser)

   def cartTotal(loginUser):
      cart = UserCart.objects.filter(user=loginUser).values()
      pre_total=[]
      for i in cart:
         
         item = Product.objects.get(pk=i['product_id'])
         cart_quantity = UserCart.objects.get(pk=i['id'])
         pre_total.append(item.product_price * cart_quantity.quantity)
      total=sum(pre_total)
      return total;
   
   total = cartTotal(loginUser)
   return render(request,'generalCart/cart.html',{'cart':cart,'total':total})



