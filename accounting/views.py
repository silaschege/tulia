from django.shortcuts import render,redirect
from cart.models import UserCart
from product.models import Product
from .forms import userShippingPaymentFrom

# Create your views here.
def userShippingPayment(request):

    def cartInfo():
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
        return total,cart;

    cart_info=cartInfo()
    print(cart_info[1])

    form = userShippingPaymentFrom
    if request.method == 'POST':
        form = userShippingPaymentFrom(request.POST)
        if form.is_valid():
           userLocation=form.save(commit=False) 
           userLocation.user = request.user
           userLocation.save()
           return redirect('UserShippingReceipt')

    return render(
                    request,
                    'userAccountingtemplate/userShippingPayment.html',
                    {'total':cart_info[0],'cart':cart_info[1],'form':form}
                )
