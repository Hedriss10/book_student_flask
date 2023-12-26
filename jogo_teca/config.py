

SECRET_KEY = "alura"

SQLALCHEMY_DATABASE_URI  = \
    '{SGDB}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGDB='mysql+mysqlconnector',  # Correção aqui
        usuario='root',
        senha='Binfae@45',
        servidor='localhost',
        database='jogoteca'
    )
