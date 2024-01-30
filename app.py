from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
Flask.secret_key = 'will'

# Tela inicial de login
@app.route('/')
def login():
    return render_template('index.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'adm' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        return redirect('/formularioidenficacao')
    else:
        return redirect('/')

# Rotas do formulário de cadastro
@app.route('/formularioidenficacao')
def formulario_de_idenficacao():
    return render_template('/formularios/formularioIdentificação.html')

@app.route('/formularioendereco')
def formulario_de_endereco():
    return render_template('/formularioEndereco.html')

@app.route('/formulariooutros')
def formulario_de_outros_dados():
    return render_template('/formularioOutrosDados.html')

app.run(debug=True)