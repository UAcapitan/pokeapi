import requests
from bs4 import BeautifulSoup

url = 'http://0.0.0.0:8000'

dict_of_pokemons = {
    '1': 'bulbasaur',
    '9': 'blastoise',
    '450': 'hippowdon'
}

def test_of_choice():
    with requests.Session() as s:
        p = s.post(url + '/auth/login/', data={
        'username': 'test',
        'password': 'testpassword123'
        })

        for i in dict_of_pokemons:
            s.get(url + f'/choice/{i}')
            response = s.get(url + '/account/')

            soup = BeautifulSoup(response.text, 'html.parser')
            text = [text.text.strip() for text in soup.find_all('h5', class_='card-title')]
            if not dict_of_pokemons[i] in text:
                assert False

        assert True

def test_of_fake_choice():
    with requests.Session() as s:
        p = s.post(url + '/auth/login/', data={
        'username': 'test',
        'password': 'testpassword123'
        })

        for i in ['909', 'test', '', '---', '-', '-100', '0']:
            response = s.get('http://127.0.0.1:8000/account/')
            soup = BeautifulSoup(response.text, 'html.parser')
            text = [text.text.strip() for text in soup.find_all('h5', class_='card-title')]
            
            s.get(url + f'/choice/{i}')

            response = s.get(url + '/account/')
            soup = BeautifulSoup(response.text, 'html.parser')
            new_text = [text.text.strip() for text in soup.find_all('h5', class_='card-title')]

            if not len(new_text) == len(text):
                assert False

        assert True
