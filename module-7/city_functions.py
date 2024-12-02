# Kyle Marlia-Conner
# Assignment 7.2

def format_city_country(city, country, population=None, language=None):
    """Return a string in the form City, Country - population xxx, Language."""
    if population and language:
        return f"{city}, {country} - population {population}, {language}"
    elif population:
        return f"{city}, {country} - population {population}"
    else:
        return f"{city}, {country}"

# Test calls
if __name__ == "__main__":
    print(format_city_country("Santiago", "Chile", 5000000, "Spanish"))
    print(format_city_country("Paris", "France", 2148000))
    print(format_city_country("Tokyo", "Japan"))
