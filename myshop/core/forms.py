from django import forms
from django.contrib.auth.models import User
from .models import Buyer, Package

class SellerRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'phone_number']

class BuyerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['name', 'phone_number']

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'price']
        
