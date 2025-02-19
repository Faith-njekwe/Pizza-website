from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField()
    address = models.TextField()
    credit_card_number = models.CharField(max_length=16, null=True, blank=True)
    credit_card_expiry = models.CharField(max_length=5, null=True, blank=True) 
    credit_card_cvv = models.CharField(max_length=4, null=True, blank=True)
    email = models.EmailField()
    


    def clean(self):
        super().clean()
        # Validate credit card number with Luhn Algorithm
        if self.credit_card_number and not UserProfile.luhn_check(self.credit_card_number):
            raise ValidationError("Invalid credit card number.")
        
        # Validate CVV
        if self.credit_card_cvv and not UserProfile.is_valid_cvv(self.credit_card_cvv):
            raise ValidationError("Invalid CVV. CVV must be 3 or 4 digits long.")
        
    @staticmethod
    def luhn_check(card_number):
        if (card_number.isdigit() and len(card_number) == 16):
            return True
    
    @staticmethod
    def is_valid_cvv(cvv):
        return cvv.isdigit() and len(cvv) in [3, 4]
    
    
#choices for pizza
class Pizza(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]
    CRUST_CHOICES = [
        ('N', 'Normal'),
        ('TH', 'Thick'),
        ('TN', 'Thin'),
        ('GF', 'Gluten Free'),
    ]
    
    SAUCE_CHOICES = [
        ('TOM', 'Tomato'),
        ('BBQ', 'BBQ'),
    ]
    CHEESE_CHOICES = [
        ('MOZ', 'Mozzarella'),
        ('VEG', 'Vegan'),
        ('LF', 'Low Fat'),
    ]
    
    TOPPING_CHOICES = [
    ('Pepperoni', 'Pepperoni'),
    ('Chicken', 'Chicken'),
    ('Ham', 'Ham'),
    ('Pineapple', 'Pineapple'),
    ('Peppers', 'Peppers'),
    ('Mushrooms', 'Mushrooms'),
    ('Onions', 'Onions'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES, default='S')
    crust = models.CharField(max_length=2, choices=CRUST_CHOICES, default='N')
    sauce = models.CharField(max_length=3, choices=SAUCE_CHOICES, default='TOM')
    cheese = models.CharField(max_length=3, choices=CHEESE_CHOICES, default='MOZ')
    toppings = models.CharField(max_length=15, choices=TOPPING_CHOICES, default='Pepperoni')
    order_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.get_size_display()} {self.get_toppings_display()} Pizza ordered by {self.user.userprofile.name}"


