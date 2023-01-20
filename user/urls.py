from django.urls import path
from .views import userLogin,merchantBioDataRegistration,primaryMerchantRegistration,userRegistration,userLogout


urlpatterns = [
    path ('Login/',userLogin, name="Login"),
    path ('Logout/',userLogout, name="Logout"),
    path ('MerchantBioDataRegistration/',merchantBioDataRegistration, name="MerchantBioDataRegistration"),
    path ('UserRegistration/',userRegistration, name="UserRegistration"),
    path ('MerchantRegistration/',primaryMerchantRegistration, name="MerchantRegistration"),

  
]