def house_price(square_feet, bedrooms, bathrooms, neighborhood, year_built):
    # Base price calculation
    price = square_feet * 100 + bedrooms * 5000 + bathrooms * 2000

    # Neighborhood adjustment
    neighborhood_factor = {
        'Urban': 1.2,
        'Suburb': 1.0,
        'Rural': 0.8,
    }
    price *= neighborhood_factor.get(neighborhood, 1.0)

    # Year built adjustment (newer houses are more expensive)
    current_year = 2025  # Update this as needed or use datetime.now().year
    age = current_year - year_built
    if age < 0:
        age = 0
    # Reduce price by 0.5% per year of age
    year_factor = 1 - 0.005 * age
    price *= year_factor

    return round(price, 2)
