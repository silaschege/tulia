from django import forms
from django.forms import ModelForm
from .models import UserAccount,MerchantBioData
from django.contrib.auth.forms import UserCreationForm
from urllib import request

class UserRegistationForm(UserCreationForm):
    email = forms.EmailField(max_length=60,help_text='Your email is required ',widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'}))
    other_name = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'}))
    date_of_birth = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = UserAccount
        fields = ('email','first_name','last_name','other_name','phone_number','date_of_birth')
    
    def __init__(self, *args, **kwargs):
        super(UserRegistationForm,self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''



class MerchantBioDataRegistrationForm(ModelForm):
    class Meta:
        model = MerchantBioData
        fields = ('email', 'merchant_name', 'country', 'county', 'town', 'street', 'major_landmark', 'industry', )
        labels = {  
                    'email':'Email',
                    'merchant_name':'Merchant Name',
                    'country':'Country',
                    'county':'County', 
                    'town':'Town', 
                    'street': 'Street', 
                    'major_landmark':'Major_landmark',
                    'industry':'Industry'
                     }
        widget = { 
                    'email': forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'})),
                    'merchant_name':forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'})),
                    'country':forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'})),
                    'county':forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'})), 
                    'town':forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'})),
                    'street': forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'})), 
                    'major_landmark':forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'})),
                    'industry':forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'})),
                  

        }