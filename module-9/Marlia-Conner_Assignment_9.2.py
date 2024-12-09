# Kyle Marlia-Conner
# Assignment 9.2

import requests
import json

# Define the SWAPI endpoint for planets
url = "https://swapi.dev/api/planets/"

def test_api_connection():
    try:
        print("Connecting to the Star Wars API...\n")
        
        # Send a GET request to the SWAPI
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Connection successful. Status code:", response.status_code)
            
            # Print the raw (non-formatted) JSON response
            print("\nResponse (no formatting):")
            print(json.dumps(response.json(), indent=4))  # Pretty-print the raw JSON response
            
            print("\nFormatted Response:")
            
            # Parse the JSON response
            planets_data = response.json()
            
            # Loop through planets and print formatted details
            for planet in planets_data['results']:
                print(f"Planet Name: {planet['name']}")
                print(f"Climate: {planet['climate']}")
                print(f"Terrain: {planet['terrain']}")
                print(f"Population: {planet['population']}")
                print(f"Rotation Period: {planet['rotation_period']} hours")
                print(f"Orbital Period: {planet['orbital_period']} days")
                print("-" * 50)  # Print separator for readability
        else:
            print(f"Error: Received status code {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred while connecting to the SWAPI: {e}")

# Main program
if __name__ == "__main__":
    test_api_connection()
