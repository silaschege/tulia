from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login,logout,authenticate
User = get_user_model()
from django.contrib import messages
from .forms import UserRegistationForm,MerchantBioDataRegistrationForm
from .models import MerchantEmployees,MerchantBioData

# Create your views here.

def userLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)
        # login the user
        if user is not None:

            login(request,user)
            # check what the user flag is
            user = request.user 
            if user.is_staff==True:
                return redirect('AddProductCategory')

            if user.is_primary_merchant==True:
                return redirect('MerchantStore')
            
            if user.is_secondary_merchant==True:
                if user.last_login==None:
                    return redirect('MerchantBioDataRegistration')
                else:
                    return redirect('MerchantStore')

            
            else:
                return redirect('AllProducts')
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again..."))	
            return redirect('login')	
            
    else:
        return render(request,'generalUserTemplates/login.html',{})

# register users directly
def userRegistration(request):
    if request.method == 'POST':
        form = UserRegistationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            account = authenticate(email=email,password=password)
            login(request,account)
            messages.info(request,('Succesfully registerd'))
            return redirect('AllProducts')
    else:
        form = UserRegistationForm()
    return render(request,'generalUserTemplates/userRegistration.html',{'form':form})

# register primary merchant
def primaryMerchantRegistration(request):
    if request.method == 'POST':
        form = UserRegistationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_primary_merchant  =True
            user.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            account = authenticate(email=email,password=password)
            login(request,account)
            messages.info(request,('Succesfully registerd'))
            return redirect('MerchantBioDataRegistration')
    else:
        form = UserRegistationForm()
    return render(request,'generalUserTemplates/merchantRegistration.html',{'form':form})

# def secondaryMerchantRegistration(request):
#     if request.method == 'POST':
#         form = UserRegistationForm(request.POST)
#         if form.is_valid():
#             user=form.save(commit=False)
#             user.is_primary_merchant  =True


# this is a function when a merchant bio data is registered 
# the merchant employee is  created if the merchant bio data is considered valid
def merchantBioDataRegistration (request):
    form = MerchantBioDataRegistrationForm(request.POST)
    if request.method == 'POST':
        form = MerchantBioDataRegistrationForm(request.POST)
        if form.is_valid():
           merchant_form=form.save(commit=False) 
           merchant_form.primary_merchant = request.user
           merchant_form.save()
           merchant_business = MerchantBioData.objects.filter( primary_merchant=request.user).last()
           print(merchant_business)
           merchant_employees=MerchantEmployees(merchant=merchant_business,employee=request.user)
           merchant_employees.save()
           return redirect('MerchantStore')
    return render(request,'generaluserTemplates/merchantBioDataRegistration.html',{'form':form})

def userLogout(request):
    logout(request)
    return redirect('Home')
	# messages.success(request, ("You Were Logged Out!"))
	
