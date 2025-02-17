from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PizzaForm(forms.ModelForm):
    #The Meta class inside a ModelForm is used to link the form to a specific Django model
    #eg form represents the pizza model, and should have its attributes
    class Meta:
        model = Pizza
        fields = ['size', 'crust', 'sauce', 'cheese', 'toppings']
        
        
    

        #def __str__(self):
            #return self.name
        
class Checkout(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'address', 'credit_card_number', 'credit_card_expiry', 'credit_card_cvv', 'email']  # Corrected 'paymentinfo'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'small-input'}),
            'address': forms.TextInput(attrs={'class': 'small-input'}),
            # Ensure other fields are appropriately configured
        }
