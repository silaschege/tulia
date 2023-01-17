from django.urls import path
from .views import userLogin,merchantBioDataRegistration,merchantRegistration,userRegistration,userLogout


urlpatterns = [
    path ('Login/',userLogin, name="Login"),
    path ('Logout/',userLogout, name="Logout"),
    path ('MerchantBioDataRegistration/',merchantBioDataRegistration, name="MerchantBioDataRegistration"),
    path ('UserRegistration/',userRegistration, name="UserRegistration"),
    path ('MerchantRegistration/',merchantRegistration, name="MerchantRegistration"),

  
]