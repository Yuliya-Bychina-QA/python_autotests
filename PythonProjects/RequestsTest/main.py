import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '7f5d21935409314019e09a0afee5e7ef'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "Melon6633",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
body_change = {
    "pokemon_id": "26301",
    "name": "Dorris",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
body_add = {
    "pokemon_id": "26301"
}

          
'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_add.text)