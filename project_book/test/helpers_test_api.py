import requests 
import json


# get http://127.0.0.1:8000/hoteis
url = "http://127.0.0.1:8000/hoteis"
response = requests.get(url)
if response.status_code == 200:
    hoteis_cadastrado = response.json()
    print(hoteis_cadastrado)
    
else:
    print(f"Erro veja o status code{response.status_code}")