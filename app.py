from flask import Flask, render_template, request, redirect, session
import sqlite3 as db

def criar_conexao():
    return db.connect('cadastro.db')

def criar_tabela_cadastro(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cadastro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            rg TEXT,
            cpf TEXT,
            orgao_expedidor TEXT,
            sexo TEXT,
            pai TEXT,
            mae TEXT,
            naturalidade TEXT,
            uf TEXT,
            pais TEXT,
            cep TEXT,
            logradouro TEXT,
            numero TEXT,
            complemento TEXT,
            bairro TEXT,
            cidade TEXT,
            telefone TEXT,
            data_nascimento TEXT,
            estado_civil TEXT,
            nome_conjuge TEXT,
            profissao TEXT,
            escolaridade TEXT,
            data_de_batismo TEXT,
            batizado_esp_santo TEXT,
            rol TEXT,
            congregacao TEXT,
            funcao TEXT,
            origem TEXT,
            situacao TEXT,
            observacao TEXT
        )
    ''')

lista_dados_cadastrais = []

class Cadastro():
    def __init__(self, uf):
        self.uf = uf

class CadastroIdentificacao(Cadastro):
    def __init__(self, nome, rg, cpf, orgao_expedidor, sexo, pai, mae, naturalidade, uf, pais):
        super().__init__(uf)
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.orgao_expedidor = orgao_expedidor
        self.sexo = sexo
        self.pai = pai
        self.mae = mae
        self.naturalidade = naturalidade
        self.pais = pais

    def mostrar(self):
        print(f'''{self.nome}, 
              {self.rg}, 
              {self.cpf}, 
              {self.orgao_expedidor}, 
              {self.sexo},
              {self.pai},
              {self.mae},
              {self.naturalidade},
              {self.pais}
              {self.uf}''')

class CadastroEndereco(Cadastro):
    def __init__(self, cep, logradouro, numero, complemento, bairro, cidade, uf, telefone):
        super().__init__(uf)
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.telefone = telefone
    
    def mostrar(self):
        print(f'''{self.cep}, 
                {self.logradouro}, 
                {self.numero}, 
                {self.complemento}, 
                {self.bairro},
                {self.cidade},
                {self.uf},
                {self.telefone},
                ''')
        
class CadastroOutros(Cadastro):
    def __init__(self, data_nascimento, estado_civil, nome_conjuge, profissao, escolaridade, data_de_batismo, batizado_esp_santo, rol, congregacao, funcao, origem, situacao, observacao):
    
        self.data_nascimento = data_nascimento
        self.estado_civil = estado_civil
        self.nome_conjuge = nome_conjuge
        self.profissao = profissao
        self.escolaridade = escolaridade
        self.data_de_batismo = data_de_batismo
        self.batizado_esp_santo = batizado_esp_santo
        self.rol = rol
        self.congregacao = congregacao
        self.funcao = funcao
        self.origem = origem
        self.situacao = situacao
        self.observacao = observacao
    
    def mostrar(self):
        print(f'''
                {self.data_nascimento}, 
                {self.estado_civil}, 
                {self.nome_conjuge}, 
                {self.profissao}, 
                {self.escolaridade},
                {self.data_de_batismo},
                {self.batizado_esp_santo},
                {self.rol},
                {self.congregacao},
                {self.funcao},
                {self.origem},
                {self.situacao},
                {self.observacao}
                ''')




app = Flask(__name__)
Flask.secret_key = 'will'

# Tela inicial de login
@app.route('/login')
def login():
    return render_template('/login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'adm' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        return redirect('/formularioidenficacao')
    else:
        return redirect('/login')
    
@app.route('/logout')
def logout():
    session['usuario_logado'] == None
    return redirect('/')

@app.route('/')
def index():
    return render_template('/index.html')

# Rotas do formulário de cadastro
@app.route('/formularioidenficacao', methods=['POST', 'GET'])
def formulario_de_idenficacao():
    if request.method == 'POST':
        nome = request.form['nome']
        rg = request.form['rg']
        cpf = request.form['cpf']
        orgao_expedidor = request.form['orgaoExpedidor']
        sexo = 'masculino'
        pai = request.form['pai']
        mae = request.form['mae']
        naturalidade = request.form['naturalidade']
        pais = request.form['pais']
        uf = request.form['estados']
        identificacao = CadastroIdentificacao(nome, rg, cpf, orgao_expedidor, sexo, pai, mae, naturalidade, pais, uf)
        lista_dados_cadastrais.append(identificacao)

        print("Dados coletados:")
        for cadastro in lista_dados_cadastrais:
            cadastro.mostrar()
        return redirect('/formularioendereco')
    else:
        return render_template('/formularios/formularioIdentificação.html')

# Cadastra dados do endereço
@app.route('/formularioendereco', methods=['POST', 'GET'])
def formulario_de_endereco():
    if request.method == 'POST':
        cep = request.form['cep']
        logradouro = request.form['logradouro']
        numero = request.form['numero']
        complemento = request.form['complemento']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        uf = request.form['uf']
        telefone = request.form['telefone']
        endereco = CadastroEndereco(cep, logradouro, numero, complemento, bairro, cidade, uf, telefone)
        lista_dados_cadastrais.append(endereco)

        print("Dados coletados:")
        for cadastro in lista_dados_cadastrais:
            cadastro.mostrar()
        return redirect('/formulariooutros')
    else:
        return render_template('/formularios/formularioEndereco.html')

# cadastrar outros dados
@app.route('/formulariooutros', methods=['POST', 'GET'])
def formulario_de_outros_dados():
    conn = criar_conexao()
    cursor = conn.cursor()

    if request.method == 'POST':


        data_nascimento = request.form['dataNascimento']
        estado_civil = request.form['estadoCivil']
        nome_conjuge = request.form['nomeConjuge']
        profissao = request.form['profissao']
        escolaridade = request.form['escolaridade']
        data_de_batismo = request.form['dataDeBatismo']
        batizado_esp_santo = 'Não'
        rol = request.form['rol']
        congregacao = request.form['congregacao']
        funcao = request.form['funcao']
        origem = request.form['origem']
        situacao = request.form['situacao']
        observacao = request.form['observacao']

        outro_dados = CadastroOutros(data_nascimento, estado_civil, nome_conjuge, profissao, escolaridade, data_de_batismo, batizado_esp_santo, rol, congregacao, funcao, origem, situacao, observacao)

        lista_dados_cadastrais.append(outro_dados)

        print("Dados coletados:")
        for cadastro in lista_dados_cadastrais:
            cadastro.mostrar()
        return redirect('/cadastrar')
    
    else:
        return render_template('/formularios/formularioOutrosDados.html')

@app.route('/cadastrar', methods=['POST', 'GET'])
def cadastrar_dados_no_banco():
    conn = criar_conexao()
    cursor = conn.cursor()
    criar_tabela_cadastro(conn)
    if request.method == 'POST':
        lista_dados = []
        for cadastro in lista_dados_cadastrais:
            if isinstance(cadastro, CadastroIdentificacao):
                dados = {
                    'nome': cadastro.nome,
                    'rg': cadastro.rg,
                    'cpf': cadastro.cpf,
                    'orgao_expedidor': cadastro.orgao_expedidor,
                    'sexo': cadastro.sexo,
                    'pai': cadastro.pai,
                    'mae': cadastro.mae,
                    'naturalidade': cadastro.naturalidade,
                    'uf': cadastro.uf,
                    'pais': cadastro.pais,
                    'cep': None,  
                    'logradouro': None,
                    'numero': None,
                    'complemento': None,
                    'bairro': None,
                    'cidade': None,
                    'telefone': None,
                    'data_nascimento': None,
                    'estado_civil': None,
                    'nome_conjuge': None,
                    'profissao': None,
                    'escolaridade': None,
                    'data_de_batismo': None,
                    'batizado_esp_santo': None,
                    'rol': None,
                    'congregacao': None,
                    'funcao': None,
                    'origem': None,
                    'situacao': None,
                    'observacao': None
                }
                lista_dados.append(dados)
            elif isinstance(cadastro, CadastroEndereco):
                dados = {
                    'nome': None,  
                    'rg': None,  
                    'cpf': None,  
                    'orgao_expedidor': None,  
                    'sexo': None,  
                    'pai': None,  
                    'mae': None, 
                    'naturalidade': None,  
                    'uf': cadastro.uf,
                    'pais': None,  
                    'cep': cadastro.cep,
                    'logradouro': cadastro.logradouro,
                    'numero': cadastro.numero,
                    'complemento': cadastro.complemento,
                    'bairro': cadastro.bairro,
                    'cidade': cadastro.cidade,
                    'telefone': cadastro.telefone,
                    'data_nascimento': None,
                    'estado_civil': None,
                    'nome_conjuge': None,
                    'profissao': None,
                    'escolaridade': None,
                    'data_de_batismo': None,
                    'batizado_esp_santo': None,
                    'rol': None,
                    'congregacao': None,
                    'funcao': None,
                    'origem': None,
                    'situacao': None,
                    'observacao': None
                }
                lista_dados.append(dados)
            elif isinstance(cadastro, CadastroOutros):
                dados = {
                    'nome': None, 
                    'rg': None, 
                    'cpf': None,  
                    'orgao_expedidor': None, 
                    'sexo': None, 
                    'pai': None, 
                    'mae': None,
                    'naturalidade': None,
                    'uf': None,
                    'pais': None,
                    'cep': None, 
                    'logradouro': None, 
                    'numero': None, 
                    'complemento': None,
                    'bairro': None, 
                    'cidade': None, 
                    'telefone': None, 
                    'data_nascimento': cadastro.data_nascimento,
                    'estado_civil': cadastro.estado_civil,
                    'nome_conjuge': cadastro.nome_conjuge,
                    'profissao': cadastro.profissao,
                    'escolaridade': cadastro.escolaridade,
                    'data_de_batismo': cadastro.data_de_batismo,
                    'batizado_esp_santo': cadastro.batizado_esp_santo,
                    'rol': cadastro.rol,
                    'congregacao': cadastro.congregacao,
                    'funcao': None,
                    'origem': None,
                    'situacao': None,
                    'observacao': None
                }
                lista_dados.append(dados)

        # Inserindo os registros da lista
        for dados in lista_dados:
            cursor.execute('''
                INSERT INTO Cadastro (nome, rg, cpf, orgao_expedidor, sexo, pai, mae, naturalidade, uf, pais, cep, logradouro, numero, complemento, bairro, cidade, telefone, data_nascimento, estado_civil, nome_conjuge, profissao, escolaridade, data_de_batismo, batizado_esp_santo, rol, congregacao, funcao, origem, situacao, observacao)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                dados.get('nome'), dados.get('rg'), dados.get('cpf'), dados.get('orgao_expedidor'), dados.get('sexo'),
                dados.get('pai'), dados.get('mae'), dados.get('naturalidade'), dados.get('uf'), dados.get('pais'),
                dados.get('cep'), dados.get('logradouro'), dados.get('numero'), dados.get('complemento'),
                dados.get('bairro'), dados.get('cidade'), dados.get('telefone'), dados.get('data_nascimento'),
                dados.get('estado_civil'), dados.get('nome_conjuge'), dados.get('profissao'), dados.get('escolaridade'),
                dados.get('data_de_batismo'), dados.get('batizado_esp_santo'), dados.get('rol'), dados.get('congregacao'),
                dados.get('funcao'), dados.get('origem'), dados.get('situacao'), dados.get('observacao')
            ))

        # Salvando as alterações
        conn.commit()

        # Fechando a conexão
        conn.close()
        return redirect('/cadastrado')
    else:
        return redirect('/naoCadastrado')

@app.route('/naoCadastrado')
def naoCadastrado():
    return render_template('formularios/erroNoCadastro.html')

# tela de finalização do cadastro de formulário
@app.route('/cadastrado')
def cadastro():
    return render_template('formularios/confirmacaoCadastro.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('/pagina_nao_encontrada.html'), 404

app.run(debug=True)


# if 'usuario_logado' not in session or session['usuario_logado'] == None:
    #     return redirect('/')