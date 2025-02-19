from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PizzaForm(forms.ModelForm):

    class Meta:
        model = Pizza
        fields = ['size', 'crust', 'sauce', 'cheese', 'toppings']
        
        
    
        
class Checkout(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'address', 'credit_card_number', 'credit_card_expiry', 'credit_card_cvv', 'email']  # Corrected 'paymentinfo'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'small-input'}),
            'address': forms.TextInput(attrs={'class': 'small-input'}),
        }
