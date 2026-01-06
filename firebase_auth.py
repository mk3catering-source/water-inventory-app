import requests

API_KEY = "AIzaSyDu3cMLDaxOL77pIAdXGfAl8n5MUcyYomc"
DB_URL = "https://waterinventoryapp-default-rtdb.firebaseio.com/"

def register_user(email, password):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API_KEY}"
    data = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    res = requests.post(url, json=data)
    return res.json()

def login_user(email, password):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
    data = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    res = requests.post(url, json=data)
    return res.json()
