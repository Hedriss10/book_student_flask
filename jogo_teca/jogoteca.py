from flask import Flask, render_template

app = Flask(__name__)

@app.route("/inicio")
def home_ola():
    list_game = ['Dota', 'Pes2012', 'Warcraft', 'Need for speed', 'SubwaySurfs']
    return render_template("lista.html", titulos='jogos', jogos=list_game)
    
if __name__ == "__main__":
    app.run(port=8000 , debug=True)
