from flask_restful import Resource, reqparse

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
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome")
    argumentos.add_argument("estrela")
    argumentos.add_argument("diaria")
    argumentos.add_argument("cidade") 

    def find_hotel(hotel_id):
        for hotel in list_hoteis:
            if hotel['hoteis_id'] == hotel_id:
                return hotel
        return None

    # função para pegar o hotel por id e usar o method get 
    def get(self, hotel_id):
        hotel =  Hotel.find_hotel(hotel_id)
        if hotel is not None:
            return hotel
        return {"message" : "hotel não existe"},  400 # page not found 


    def post(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        novo_hotel =  { 'hoteis_id' : hotel_id, **dados}
        list_hoteis.append(novo_hotel)    
        return novo_hotel, 200 # sucess
        
        
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        novo_hotel =  {"hoteis_id" : hotel_id, **dados}
        hotel =  Hotel.find_hotel(hotel_id)
        if hotel is not None:
            hotel.update(novo_hotel)
            return hotel, 200 # 
        list_hoteis.append(novo_hotel)
        return novo_hotel, 201 #  
    
    
    
    def delete(self, hotel_id):
        global list_hoteis
        list_hoteis = [hotel for hotel in list_hoteis if hotel["hoteis_id"] != hotel_id]
        return {"message" : "Hotel Deletado com sucesso!"}