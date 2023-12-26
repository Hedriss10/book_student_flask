from flask import Flask, render_template, request, redirect
from flask import flash , session




class Jogos:
    def __init__(self, name, console, categoria):
        self.name =  name 
        self.console = console
        self.categoria = categoria


# passando a quantidade de jogos que teremos
jogo1 = Jogos(name="Dota", console="PC", categoria="RPG")
jogo2 = Jogos(name="Warcraft", console="PC", categoria="RPG")
jogo3 = Jogos(name="LOL", console="PC", categoria="RPG")
list_game = [jogo1, jogo2, jogo3]


app = Flask(__name__)
app.secret_key = "student_flask"



@app.route("/")
def index():
    return render_template("lista.html", titulos='jogos', jogos=list_game)
    

@app.route("/novo")
def novo():
    return render_template("novo.html", titulo="Novos jogos")
    

@app.route("/criar", methods=["POST", ])
def criar():
    nome = request.form["nome"]
    categoria = request.form["categoria"]
    console = request.form["console"]
    novo_jogo = Jogos(name=nome, categoria=categoria, console=console)
    list_game.append(novo_jogo)
    return redirect("/")

@app.route("/login")
def login():
    return render_template("login.html")



@app.route("/autenticar", methods=["POST", ])
def autenticar():
    if "senhafacil" == request.form["senha"]:
        # Colocando o session no flask para ter um aviso para o usuario 
        session["usuario_logado"] =  request.form["usuario"]
        flash(session["usuario_logado"] +  " logado com sucesso.")
        
        return redirect("/")
    else:
        flash("Usuário não logado.")
        return redirect("/login")
    
    
    
@app.route("/logout")
def logout():    
    session["usuario_logado"] = None
    flash("Usuário deslogado com sucesso.")
    return redirect("/")


if __name__ == "__main__":
    app.run(port=8000 , debug=True)
