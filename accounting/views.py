from django.shortcuts import render,redirect
from cart.models import UserCart
from product.models import Product
from .forms import userShippingPaymentFrom
from shipping.models import userShippingNumber,userShippingItems


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

    form = userShippingPaymentFrom
    if request.method == 'POST':
        form = userShippingPaymentFrom(request.POST)
        if form.is_valid():
           userLocation=form.save(commit=False) 
           userLocation.user = request.user
           userLocation.save()
           

    def createShippingDetails():
        loggedInUser = request.user
        userShippingNumber.objects.create(user=loggedInUser,total=cart_info[0],prepare=True,on_transit=False,delivered=False)
        shippingNumber = userShippingNumber.objects.filter(user=loggedInUser).last()
        for i in cart_info[1]:
            userShippingItems.objects.create(shipping_number=shippingNumber,product=i.product,quantity=i.quantity)
            UserCart.objects.filter( user=loggedInUser,product=i.product).delete()
            print('usercart succesfull')
            
        return redirect('UserShippingReceipt')
    
    createShippingDetails()


    return render(
                    request,
                    'userAccountingtemplate/userShippingPayment.html',
                    {'total':cart_info[0],'cart':cart_info[1],'form':form}
                )

# there should be changes for tpe of payment which should be choice field connected to a table for each table method

def userShippingReceipt(request):
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
    return render(request,'userAccountingtemplate/userShippingReceipt.html',{'total':cart_info[0],'cart':cart_info[1],})
