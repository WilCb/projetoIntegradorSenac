from flask import session, url_for, render_template, request, redirect, flash
from app import app, criar_conexao

@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    return render_template('/index.html')


@app.route('/formulario-de-cadastro', methods=['POST', 'GET'])
def formulario_de_cadastro():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=formulario-de-cadastro')
    elif request.method == 'POST':
        try:
            conexao = criar_conexao()
            cursor = conexao.cursor()

            pegar_dados_do_formulario = [
                request.form['nome'].upper().lstrip().rstrip(
                ), request.form['rg'], request.form['cpf'], request.form['orgaoExpedidor'],
                request.form['sexo'].upper().lstrip().rstrip(
                ), request.form['pai'], request.form['mae'], request.form['naturalidade'],
                request.form['ufIdentidade'], request.form['pais'], request.form['cep'].replace(
                    '-', ''), request.form['logradouro'], request.form['numero'], request.form['complemento'],
                request.form['bairro'].upper().lstrip().rstrip(), request.form['cidade'], request.form['ufEndereco'], request.form['telefone'],
                request.form['dataNascimento'], request.form['estadoCivil'], request.form['nomeConjuge'],
                request.form['profissao'].upper().lstrip().rstrip(
                ), request.form['escolaridade'], request.form['dataDeBatismo'],
                request.form['batismo'], request.form['rol'], request.form['congregacao'], request.form['funcao'],
                request.form['origem'], request.form['situacao'], request.form['observacao']
            ]

            # Inserindo os dados no banco de dados
            cursor.execute("""
                INSERT INTO cadastro (nome, rg, cpf, orgao_expedidor, sexo, pai, mae, naturalidade, uf_identidade, 
                pais, cep, logradouro, numero, complemento, bairro, cidade, uf_endereco, telefone, data_nasc, 
                estado_civil, nome_conjuge, profissao, escolaridade, data_batismo, batizado_esp_santo, 
                entrada_rol_membros, congregacao, funcao, origem, situacao, igreja_cidade) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, pegar_dados_do_formulario)

            conexao.commit()
            cursor.close()
            conexao.close()
            return redirect(url_for('cadastrado'))
        except Exception as e:
            print("Erro ao inserir no banco de dados:", e)
            return redirect(url_for('erro_no_cadastro'))
    else:
        return render_template('/formulario.html')


@app.route('/cadastrado')
def cadastrado():
    return render_template('erros/confirmacao_de_cadastro.html')


@app.route('/lista-de-membros', methods=['GET', 'POST'])
def listarMembros():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    elif request.method == 'POST':
        filtro = request.form['filtro']

        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            'SELECT nome, rg, cpf, orgao_expedidor, pai, mae FROM cadastro', ('%' + filtro + '%',))
        resultados = cursor.fetchall()
        conexao.close()

        return render_template('/listar_membros.html', resultados=resultados)
    return render_template('/listar_membros.html')


@app.route('/consultar-membro', methods=['GET', 'POST'])
def consultarMembro():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=consultar-membro')
    elif request.method == 'POST':
        buscaPorCpf = request.form['buscaPorCpf']

        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT nome, rg, orgao_expedidor, sexo, pai, mae, naturalidade, uf_identidade, pais, cep, logradouro, numero, complemento, bairro, cidade, uf_endereco, telefone FROM cadastro WHERE cpf = (%s)', (buscaPorCpf,))
        # data_nasc, estado_civil, nome_conjuge, profissao, escolaridade, data_batismo, batizado_esp_santo, entrada_rol_membros, congregacao, funcao, origem, situacao, igreja_cidade FROM cadastro'
        resultados = cursor.fetchall()
        conexao.close()

        return render_template('/consultar_membro.html', resultados=resultados)
    return render_template('/consultar_membro.html')


@app.route('/erro-no-cadastro')
def erro_no_cadastro():
    return render_template('/erros/erro_no_cadastro.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('erros/pagina_nao_encontrada.html'), 404

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('/login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'adm' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] == None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('login'))
