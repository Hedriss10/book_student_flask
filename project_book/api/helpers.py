import requests 
import json

# Testando API em Flask

url = "http://127.0.0.1:8000/hoteis"

response =  requests.get(url)

if response.status_code == 200:
    hoteis_cadastrados = response.json()
    print(hoteis_cadastrados)

else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")
