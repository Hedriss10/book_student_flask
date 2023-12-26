from flask import Flask, render_template, request
from flask import redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'alura'
app.config["SQLACLHEMY_DATABASE_URI"] = \
    '{SGDB}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'Binfae@45',
        servidor = 'localhost',
        database = 'jogoteca'  
    )

db = SQLAlchemy(app)





app.run(debug=True)