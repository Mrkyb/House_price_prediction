from django.db import models
from django.contrib.auth.models import User

class HousePricePrediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    square_feet = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    neighborhood = models.CharField(max_length=50)
    year_built = models.IntegerField()
    predicted_price_usd = models.DecimalField(max_digits=12, decimal_places=2)
    predicted_price_tsh = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction for {self.square_feet} sqft in {self.neighborhood}"

    class Meta:
        ordering = ['-created_at']
