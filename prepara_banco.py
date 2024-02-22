import psycopg2
from flask_bcrypt import generate_password_hash


print('Conectando...')
try:
    conn = psycopg2.connect(
        host='localhost',
        database='igreja',
        user='postgres',
        password='1234'
    )

except psycopg2.Error as err:
    print(err)

cursor = conn.cursor()

# criando tabelas
TABLES = {}

TABLES['Cadastro'] = ('''
    CREATE TABLE IF NOT EXISTS cadastro (
        ID serial PRIMARY KEY,
        nome character(70) NOT NULL,
        rg varchar(11) NOT NULL,
        cpf varchar(11) NOT NULL,
        orgao_expedidor character(20) NOT NULL,
        sexo character(10) NOT NULL,
        pai character(70) NOT NULL,
        mae character(70) NOT NULL,
        naturalidade character(70) NOT NULL,
        uf_identidade character(30) NOT NULL,
        pais text NOT NULL,
        cep varchar(8) NOT NULL,
        logradouro character(70) NOT NULL,
        numero numeric(5) NOT NULL,
        complemento character(25),
        bairro character(60) NOT NULL,
        cidade character(50) NOT NULL,
        uf_endereco character(30) NOT NULL,
        telefone numeric(13) NOT NULL,
        data_nascimento date NOT NULL,
        estado_civil character(25) NOT NULL,
        nome_conjuge character(50),
        profissao character(50) NOT NULL,
        escolaridade character(50) NOT NULL,
        data_batismo date,
        batizado_esp_santo character(3) NOT NULL,
        entrada_rol_membros date,
        congregacao numeric(100) NOT NULL,
        funcao character(25) NOT NULL,
        origem character(25) NOT NULL,
        situacao character(30),
        igreja_cidade text
    )
''')

TABLES['Usuarios'] = ('''
    CREATE TABLE IF NOT EXISTS usuarios (
        ID serial PRIMARY KEY,
        nome varchar(20) NOT NULL,
        senha varchar(100) NOT NULL
    ) 
''')

for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print(f'Criando tabela {tabela_nome}', end=' ')
        cursor.execute(tabela_sql)
    except psycopg2.Error as err:
        print(err)
    else:
        print('ok')

# inserindo usuarios
usuarios_sql = 'INSERT INTO usuarios (nome, senha) VALUES (%s, %s)'
usuarios = [
    ('ADM', generate_password_hash('ADM#2024').decode('utf-8'))
]
cursor.executemany(usuarios_sql, usuarios)
conn.commit()

cursor.close()
conn.close()