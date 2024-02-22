from flask import session, url_for, render_template, redirect, request
from app import app, db
from sqlalchemy import func, table, column, select
from models import Cadastro
from helpers import FormularioCadastro
from datetime import date
@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('index')))
    
    form = FormularioCadastro()
    total_de_membros = db.session.query(func.count(Cadastro.id)).scalar()
    membros = Cadastro.query.filter_by(id=Cadastro.id)

    # Manipulação da data
    mes = date.today().month
    data = date.today()
    dataFormatada = data.strftime('%d/%m/%Y')
    aniversariante = Cadastro.query.filter(func.extract('month', Cadastro.data_nascimento) == mes).all()
    # ----------------------------


    return render_template('index.html', form=form, total_de_membros=total_de_membros, aniversariante=aniversariante, data_atual=dataFormatada, membros=membros)

@app.route('/erro-no-cadastro')
def erro_no_cadastro():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('formulario_de_cadastro')))
    return render_template('/erros/erro_no_cadastro.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('erros/pagina_nao_encontrada.html'), 404


