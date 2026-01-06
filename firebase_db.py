import requests

DB_URL = "https://waterinventoryapp-default-rtdb.firebaseio.com/"

def get_stock(size, token):
    url = f"{DB_URL}/inventory/{size}.json?auth={token}"
    res = requests.get(url)
    return res.json()

def update_stock(size, value, token):
    url = f"{DB_URL}/inventory/{size}.json?auth={token}"
    requests.put(url, json=value)
