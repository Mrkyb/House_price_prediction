from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
  # Import the prediction history view


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('predict/', views.house_price_prediction, name='house_price_prediction'),
    path('history/', views.prediction_history, name='prediction_history'),
    path('history/export/', views.export_predictions_csv, name='export_predictions'),
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset.html'),
         name='password_reset'),
    path('password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]