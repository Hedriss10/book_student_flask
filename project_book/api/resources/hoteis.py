from flask_restful import Resource



list_hoteis = [
    {
        'hoteis_id': 'alpha',
        'nome': 'Bucanas de lux',
        'estrela': '10',
        'diaria': '200R$',
        'cidade': 'Rio de Janeiro',
        
    },
    {
        'hoteis_id': 'bravo',
        'nome': 'Bucanas de lux',
        'estrela': '10',
        'diaria': '200R$',
        'cidade': 'Rio de Janeiro',
        
    },
    {
        'hoteis_id': 'charlie',
        'nome': 'Bucanas de lux',
        'estrela': '10',
        'diaria': '200R$',
        'cidade': 'Rio de Janeiro',
        
    },    

]


class Hoteis(Resource):
    def get(self):
        return {"hoteis" : list_hoteis}
    
    
class Hotel(Resource):

    # função para pegar o hotel por id e usar o method get 
    def get(self, hotel_id):
        for hotel in list_hoteis:
            if hotel['hoteis_id'] == hotel_id:
                return hotel
        return {"message" : "hotel não existe"},  400 # page not found 


    def post(self, hotel_id):
        ...
        
    def delete(self, hotel_id):
        ...
        
    def put(self, hotel_id):
        ...
