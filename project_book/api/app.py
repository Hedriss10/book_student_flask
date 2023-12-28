from flask import Flask 
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)



class Hoteis(Resource):
    """
        Class Hoteis que está herdando de Resource 
    """
    def get(self):
        """
        Função para lê todos os Hoteis do banco dee dados usando o métedo simples GET.
        """
        return {"hoteis" : "Tem 10 hoteis cadastrado no banco de dados.."}
    

api.add_resource(Hoteis, "/hoteis")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
    
    
    
# ROTA PARA API =  http://127.0.0.1:8000