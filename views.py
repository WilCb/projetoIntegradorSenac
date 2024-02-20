from flask import session, url_for, render_template, redirect
from app import app, db
from sqlalchemy import func
from models import Cadastro

@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('index')))
    contagem = db.session.query(func.count(Cadastro.id))
    return render_template('index.html', contagem=contagem)

@app.route('/erro-no-cadastro')
def erro_no_cadastro():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('formulario_de_cadastro')))
    return render_template('/erros/erro_no_cadastro.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('erros/pagina_nao_encontrada.html'), 404


