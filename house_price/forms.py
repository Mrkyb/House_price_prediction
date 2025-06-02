from django import forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


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
