# Kyle Marlia-Conner
# Assignment 9.2

import requests

# URL for API to get info about astronauts
url = "http://api.open-notify.org/astros.json"

def fetch_astronauts():
    try:
        # Make a GET request to the API
        response = requests.get(url)
        # Check for successful response
        if response.status_code == 200:
            data = response.json()  # Parse JSON response
            return data
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_astronauts(data):
    print("\nCurrent Astronauts in Space:")
    print(f"Number of astronauts: {data['number']}")
    for astronaut in data['people']:
        print(f"- {astronaut['name']} on {astronaut['craft']}")

# Main program
if __name__ == "__main__":
    print("Fetching data from OpenNotify API...")
    astronauts_data = fetch_astronauts()
    if astronauts_data:
        display_astronauts(astronauts_data)
    else:
        print("Failed to retrieve data.")
