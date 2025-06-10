from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class signupform(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    terms_agreed = forms.BooleanField(required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords don't match")

        if User.objects.filter(username=cleaned_data.get('username')).exists():
            raise ValidationError("Username already exists")

        if User.objects.filter(email=cleaned_data.get('email')).exists():
            raise ValidationError("Email already registered")

        return cleaned_data
    
from django import forms

class HousePriceForm(forms.Form):
    SquareFeet = forms.IntegerField(label='Size of the house (in Square Feet)', min_value=1)
    bedrooms = forms.IntegerField(label='Number of Bedrooms', min_value=1)
    bathrooms = forms.IntegerField(label='Number of Bathrooms', min_value=1)
    
    NEIGHBORHOOD_CHOICES = [
        ('Urban', 'Urban'),
        ('Suburb', 'Suburb'),
        ('Rural', 'Rural'),
    ]
    neighborhood = forms.ChoiceField(label='Neighborhood', choices=NEIGHBORHOOD_CHOICES)
    
    year_built = forms.IntegerField(label='Year the house was built', min_value=1000, max_value=9999)