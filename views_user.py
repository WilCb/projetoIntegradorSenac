from app import app
from flask import request, render_template, redirect, session, url_for, flash
from helpers import FormularioUsuario
from models import Usuarios
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    try:
        form = FormularioUsuario(request.form)
        usuario = Usuarios.query.filter_by(nome=form.nome.data).first()
        senha = check_password_hash(usuario.senha, form.senha.data)
        if usuario and senha:
            session['usuario_logado'] = usuario.nome
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash('Usuário não logado.')
            return redirect(url_for('login'))
    except AttributeError:
        flash('Acesso inválido !')
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('login'))