from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.urls import reverse  # ADD THIS IMPORT
import pandas as pd
from .forms import HousePriceForm
from .utils import house_price
from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    next_page = 'login'  # Set default redirect


def get_dataset():
    try:
        return pd.read_csv(settings.BASE_DIR / 'house_price' / 'housing_price_dataset.csv')
    except Exception as e:
        print(f"Dataset loading failed: {e}")
        return None

from django.utils.http import url_has_allowed_host_and_scheme

def user_login(request):
    print(f"User authenticated: {request.user.is_authenticated}")
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me') == 'on'
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # FIXED: auth_login should be defined
            
            # Handle "Remember Me"
            if not remember_me:
                request.session.set_expiry(0)  # Session expires on browser close
            
            # Handle redirect
            next_url = request.POST.get('next', '')
            if next_url and url_has_allowed_host_and_scheme(
                url=next_url,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure(),
            ):
                return redirect(next_url)
            return redirect('house_price_prediction')
        else:
            messages.error(request, "Invalid username or password.")
    
    # Get next parameter safely
    next_param = request.GET.get('next', '')
    if next_param and not url_has_allowed_host_and_scheme(
        url=next_param,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        next_param = ''
    
    return render(request, 'registration/login.html', {
        'next': next_param or reverse('house_price_prediction')  # Now reverse is imported
    })   

def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()
        terms_agreed = request.POST.get('terms') == 'on'

        try:
            if not all([username, email, password, confirm_password]):
                raise ValueError("All fields are required")
            if len(password) < 8:
                raise ValueError("Password must be at least 8 characters")
            if password != confirm_password:
                raise ValueError("Passwords don't match")
            try:
                validate_email(email)
            except ValidationError:
                raise ValueError("Invalid email format")
            if not terms_agreed:
                raise ValueError("You must accept the terms")
            if User.objects.filter(username=username).exists():
                raise ValueError("Username already exists")
            if User.objects.filter(email=email).exists():
                raise ValueError("Email already registered")

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.full_clean()
            auth_login(request, user)  # Changed to auth_login for consistency
            return redirect('house_price_prediction')

        except Exception as e:
            messages.error(request, str(e))
            return render(request, 'registration/signup.html', {
                'username': username,
                'email': email
            })
    return render(request, 'registration/signup.html')

@login_required(login_url='login')
def house_price_prediction(request):
    predicted_price_usd = None
    predicted_price_tsh = None
    closest_match = None
    form = HousePriceForm(request.POST or None)
    dataset = get_dataset()

    if request.method == 'POST' and form.is_valid():
        try:
            data = form.cleaned_data
            predicted_price_usd = house_price(
                data['SquareFeet'],
                data['bedrooms'],
                data['bathrooms'],
                data['neighborhood'],
                data['year_built']
            )
            
            if predicted_price_usd is None or predicted_price_usd < 0:
                raise ValueError("Invalid prediction result")
                
            rate = getattr(settings, 'USD_TO_TSH_RATE', 2600)
            predicted_price_tsh = predicted_price_usd * rate
            
            if dataset is not None:
                filtered = dataset[
                    (dataset['Neighborhood'] == data['neighborhood']) &
                    (dataset['Bedrooms'] == data['bedrooms'])
                ]
                if not filtered.empty:
                    idx = (filtered['SquareFeet'] - data['SquareFeet']).abs().idxmin()
                    closest_match = filtered.loc[idx].to_dict()
            
        except Exception as e:
            messages.error(request, f"Prediction error: {str(e)}")

    return render(request, 'house_price/house_price.html', {
        'form': form,
        'predicted_price_usd': f"${predicted_price_usd:,.2f}" if predicted_price_usd else None,
        'predicted_price_tsh': f"TSh {predicted_price_tsh:,.0f}" if predicted_price_tsh else None,
        'closest_match': closest_match,
    })