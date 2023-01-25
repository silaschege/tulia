from django import forms
from django.forms import ModelForm
from urllib import request
from .models import userShippingLocation

class addUserShippingLocationForm(ModelForm):
    class Meta:
        model = userShippingLocation
        fields = ('country','county','town','estate','street','major_landmark',)
        labels = {  
                'country':'Country',
                'county':'County',
                'town':'Town',
                'estate':'Estate',
                'street':'Street',
                'major_landmark':'Major Landmark',
                }
        widget = { 
                'country':forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'})),
                'county':forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'})),
                'town':forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'})),
                'estate':forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'})),
                'street':forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'})),
                'major_landmark':forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control'})),
        }