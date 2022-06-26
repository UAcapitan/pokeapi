import requests

url = 'http://0.0.0.0:8000'

list_users_for_registration = [
    {'username': 'test4', 'email': 'test@gmail.com', 'password1': 'Mypassword777', 'password2': 'Mypassword777'},
    {'username': 'test5', 'email': 'test@gmail.com', 'password1': 'Mypassword777', 'password2': 'Mypassword777'},
    {'username': 'test9', 'email': 'test@gmail.com', 'password1': 'Mypassword777', 'password2': 'Mypassword777'}
]

list_not_users_for_registration = [
    {'username': 'admin', 'email': 'test1@gmail.com', 'password1': '', 'password2': 'Mypassword777'},
    {'username': 'test01', 'email': 'test2@gmail.com', 'password1': '', 'password2': ''},
    {'username': 'test01', 'email': 'test3@gmail.com', 'password1': '1234qweqweqwe', 'password2': '1234qweqweqw'}
]

def test_if_can_register_profile():
    for i in list_users_for_registration:
        response = requests.post(url + '/auth/reg/', data=i)
        if not response.status_code == 200:
            assert False
    assert True

def test_if_not_can_register_profile():
    for i in list_not_users_for_registration:
        response = requests.post(url + '/auth/reg/', data=i)
        if not response.status_code != 200:
            assert False
    assert True