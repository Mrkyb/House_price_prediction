"""
URL configuration for myproject project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from house_price.views import user_login  # Import the login view
from house_price.views import user_signup  # Import the signup view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/login/', permanent=True)),  # Root redirect to login
    path('', include('house_price.urls')),  # Include app URLs
    
   # Authentication URLs (if not already in house_price.urls)
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)