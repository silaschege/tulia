from django.shortcuts import render,redirect
from .models import userShippingLocation,userShippingNumber,userShippingItems
from .forms import addUserShippingLocationForm

# Create your views here.
def addUserShippingLocation(request):
    form = addUserShippingLocationForm
    if request.method == 'POST':
        form = addUserShippingLocationForm(request.POST)
        if form.is_valid():
           userLocation=form.save(commit=False) 
           userLocation.user = request.user
           userLocation.save()
           return redirect('UserShippingPayment')
    return render(request,'userShippingTemplates/shippingCheckout.html',{'form':form})

def userShippingReceipt(request):
    return render(request,'userShippingTemplates/userShippingReceipt.html',{})


