import requests

def get_country_info():
    country_name = input("Enter the name of the country: ")
    response = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
    data = response.json()

    if response.status_code == 200:
        # Extract some information about the country
        country = data[0]
        name = country['name']['common']
        capital = country['capital'][0]
        area = country['area']
        population = country['population']
        languages = ', '.join(list(country['languages'].values()))
        
        print(f"\nCountry: {name}")
        print(f"Capital: {capital}")
        print(f"Area: {area} sq km")
        print(f"Population: {population}")
        print(f"Languages: {languages}")
    else:
        print(f"Country '{country_name}' not found. Please enter a valid country name.")

get_country_info()
