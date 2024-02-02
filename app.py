from flask import Flask
import psycopg2


def criar_conexao():
    conecta = psycopg2.connect(host='localhost', dbname='igreja', user='postgres', password='1234')
    return conecta

app = Flask(__name__)
Flask.secret_key = 'will'

from views import *

if __name__ == '__main__':
    app.run(debug=True)