# How to connect to an API using Python

import requests # to API request

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response_object = requests.get(url)
    print(response_object)
    
    if response_object.status_code == 200: # 200 means Response is OK
        print("Data retrieved!")
        pokemmon_data = response_object.json() # returns dictionary
        return pokemmon_data
    else:
        print(f"Failed to retrieve data {response_object.status_code}")

pokemon_name = input("Enter name of pokemon: ")
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"ID: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")
    
