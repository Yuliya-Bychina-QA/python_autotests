import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '7f5d21935409314019e09a0afee5e7ef'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '2682'


def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == '2682'
