import requests
import json
print('Poke Api')

pokeNumber = input("Enter Poke id: \n ")

pokeUrl = "http://pokeapi.co/api/v2/pokemon/" + pokeNumber

data = requests.get(pokeUrl).json()

print('Poke name : ')
print(data["abilities"][0]["ability"]["name"])


