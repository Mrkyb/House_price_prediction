from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin
from .models import HousePricePrediction

@admin.register(HousePricePrediction)
class HousePricePredictionAdmin(admin.ModelAdmin):
    list_display = ('user', 'square_feet', 'bedrooms', 'bathrooms', 'neighborhood', 'predicted_price_usd', 'created_at')
    list_filter = ('neighborhood', 'created_at')
    search_fields = ('user__username', 'neighborhood')