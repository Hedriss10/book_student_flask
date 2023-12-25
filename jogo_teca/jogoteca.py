from flask import Flask, render_template




class Jogos:
    def __init__(self, name, console, categoria):
        self.name =  name 
        self.console = console
        self.categoria = categoria




app = Flask(__name__)

@app.route("/inicio")
def home_ola():
    
    # passando a quantidade de jogos que teremos
    jogo1 = Jogos(name="Dota", console="PC", categoria="RPG")
    jogo2 = Jogos(name="Warcraft", console="PC", categoria="RPG")
    jogo3 = Jogos(name="LOL", console="PC", categoria="RPG")
    
    list_game = [jogo1, jogo2, jogo3]
    
    return render_template("lista.html", titulos='jogos', jogos=list_game)
    
if __name__ == "__main__":
    app.run(port=8000 , debug=True)
