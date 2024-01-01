import requests

    
list_hotels =  {
    'hoteis_id': 'delta',
    'nome': 'Bucanas de lux',
    'estrela': '10',
    'diaria': '200R$',
    'cidade': 'Rio de Janeiro',
}


url = f"http//127.0.0.1:5000/hoteis/{list_hotels}"
response =  requests.post(url=url)

if response.status_code ==  200:
    print(response.json())
    
else:
    print("Acesso negado")