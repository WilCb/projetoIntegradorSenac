from app import db

class Cadastro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(70), nullable=False)
    rg = db.Column(db.BigInteger, nullable=False)
    cpf = db.Column(db.BigInteger, nullable=False)
    orgao_expedidor = db.Column(db.String(20), nullable=False)
    sexo = db.Column(db.String(10), nullable=False)
    pai = db.Column(db.String(70), nullable=False)
    mae = db.Column(db.String(70), nullable=False)
    naturalidade = db.Column(db.String(70), nullable=False)
    uf_identidade = db.Column(db.String(2), nullable=False)
    pais = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.BigInteger, nullable=False)
    logradouro = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.BigInteger, nullable=False)
    complemento = db.Column(db.String(100))
    bairro = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    uf_endereco = db.Column(db.String(2), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    estado_civil = db.Column(db.String(20), nullable=False)
    nome_conjuge = db.Column(db.String(70))
    profissao = db.Column(db.String(50), nullable=False)
    escolaridade = db.Column(db.String(20), nullable=False)
    data_batismo = db.Column(db.Date)
    batizado_esp_santo = db.Column(db.String(3))
    entrada_rol_membros = db.Column(db.Date)
    congregacao = db.Column(db.BigInteger, nullable=False)
    funcao = db.Column(db.String(20), nullable=False)
    origem = db.Column(db.String(20), nullable=False)
    situacao = db.Column(db.String(20), nullable=False)
    igreja_cidade = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=True)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name