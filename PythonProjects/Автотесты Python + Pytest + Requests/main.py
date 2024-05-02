import requests

URL = 'https://api.pokemonbattle.me/v2'
HEADER = {'Content-Type': 'application/json', "trainer_token": "76424bf4ea1465432ec5fab419b80058"}
body1 = {
    "name": "generate",
    "photo": "generate"
}

body2= {
    "pokemon_id": "24184",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/012.png"
}

body3= {
    "pokemon_id": "24184"
}

responce = requests.post(url=f'{URL}/pokemons', json=body1, headers=HEADER)
print(f'Статус код: {responce.status_code}. Cообщение: {responce.json()["message"]}. id: {responce.json()["id"]}') 

responce = requests.put(url=f'{URL}/pokemons', json=body2, headers=HEADER)
print(f'Статус код: {responce.status_code}. Сообщение: {responce.json()["message"]}')

responce = requests.post(url=f'{URL}/trainers/add_pokeball', json=body3, headers=HEADER)
print(f'Статус код: {responce.status_code}. Сообщение: {responce.json()["message"]}')