import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'be33458fb019573698afe935c3400d2e'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "dmitry.danchenko2016@yandex.ru",
    "password": "Iloveqa1111"
}


body_confirmation = {
    "trainer_token": TOKEN
}


body_create = {
    "name": "Бульбазавр",
    "photo_id": 12
}

body_new_name = {
    "pokemon_id": "334447",
    "name": "Dimooon",
    "photo_id": 12
}

body_add_pokeball = {
    "pokemon_id": "334447"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print (response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''


'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)'''


'''response_new_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_new_name)
print(response_new_name.text)

message = response_new_name.json()['message']
print(message)'''


response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)

message = response_add_pokeball.json()['message']
print(message)
