from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, SelectField, IntegerField, DateField, TelField, TextAreaField, ValidationError

class FormularioCadastro(FlaskForm):
    nome = StringField('Nome', [validators.DataRequired(), validators.Length(min=3, max=70)])
    rg = IntegerField('RG', [validators.DataRequired()])
    cpf = IntegerField('CPF', [validators.DataRequired()])
    orgao_expedidor = StringField('Orgão Expedidor', [validators.DataRequired(), validators.Length(min=3, max=20)])
    sexo = SelectField('Função', [validators.DataRequired()], choices=[
        ('', 'Selecione'),
        ('MASCULINO', 'MASCULINO'),
        ('FEMININO', 'FEMININO')
    ])
    pai = StringField('Pai', [validators.DataRequired(), validators.Length(min=3, max=70)])
    mae = StringField('Mãe', [validators.DataRequired(), validators.Length(min=3, max=70)])
    naturalidade = StringField('Naturalidade', [validators.DataRequired(), validators.Length(min=3, max=70)])
    ufIdentidade = SelectField('UF Identidade', [validators.DataRequired()], choices=[
        ('', 'Selecione'),
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    ])
    pais = StringField('País', [validators.DataRequired(), validators.Length(min=2, max=50)])
    cep = IntegerField('CEP', [validators.DataRequired()])
    logradouro = StringField('Logradouro', [validators.DataRequired(), validators.Length(min=1, max=100)])
    numero = IntegerField('N: ', [validators.DataRequired()])
    complemento = StringField('Complemento', [validators.Length(max=100)])
    bairro = StringField('Bairro', [validators.DataRequired(), validators.Length(min=1, max=100)])
    cidade = StringField('Cidade', [validators.DataRequired(), validators.Length(min=1, max=50)])
    ufEndereco = SelectField('UF', [validators.DataRequired()], choices=[
        ('', 'Selecione'),
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    ])
    telefone = TelField('Telefone', [validators.DataRequired(), validators.Length(min=1, max=13)])
    dataNascimento = DateField('Data de Nascimento', [validators.DataRequired()])
    estadoCivil = SelectField('Estado Civil', [validators.DataRequired()], choices=[
        ('', 'Selecione'),
        ('Solteiro', 'Solteiro'),
        ('Casado', 'Casado'),
        ('Divorciado', 'Divorciado'),
        ('Viúvo', 'Viúvo'),
        ('Separado Judicialmente', 'Sep. Judicialmente')
    ])
    nomeConjuge = StringField('Nome do Cônjuge', [validators.Length(min=1, max=70)])
    profissao = StringField('Profissão', [validators.DataRequired(), validators.Length(min=1, max=50)])
    escolaridade = SelectField('Escolaridade', [validators.DataRequired()], choices=[
        ('', 'Selecione'),
        ('Analfabeto', 'Analfabeto'),
        ('Alfabetizado', 'Alfabetizado'),
        ('Primário', 'Primário'),
        ('1° Grau', '1° Grau'),
        ('2° Grau', '2° Grau'),
        ('Superior', 'Superior')
    ])
    dataDeBatismo = DateField('Data de batismo')
    batizado = SelectField('Batizado no Espírito Santo?', [validators.DataRequired()], choices=[
        ('', 'Selecione'),
        ('SIM', 'SIM'),
        ('NÃO', 'NÃO')
    ])
    entradaRol = DateField('Entrada no ROL')
    congregacao = IntegerField('Congregação', [validators.DataRequired()])
    funcao = SelectField('Função', [validators.DataRequired()], choices=[
        ('', 'Selecione'),
        ('PASTOR', 'PASTOR'),
        ('EVANGELISTA', 'EVANGELISTA'),
        ('PRESBÍTERIO', 'PRESBÍTERIO'),
        ('DIÁCONO', 'DIÁCONO'),
        ('AUXILIAR', 'AUXILIAR'),
        ('MEMBRO', 'MEMBRO')
    ])
    origem = SelectField('Origem', [validators.DataRequired()], choices=[
        ('', 'Selecione'),
        ('BATISMO', 'BATISMO'),
        ('TRANFERÊNCIA', 'TRANFERÊNCIA'),
        ('PRESBÍTERIO', 'PRESBÍTERIO'),
        ('ACLAMAÇÃO', 'ACLAMAÇÃO'),
        ('CONGREGAÇÃO', 'CONGREGAÇÃO')
    ])
    situacao = SelectField('Situação', [validators.DataRequired()], choices=[
        ('', 'Selecione'),
        ('ATIVO', 'ATIVO'),
        ('DISCIPLINADO', 'DISCIPLINADO'),
        ('TRANSFERIDO', 'TRANSFERIDO'),
        ('FALECIDO', 'FALECIDO'),
        ('CAND. BATISMO', 'CAND. BATISMO'),
        ('DESVIADO', 'DESVIADO'),
        ('CONGREGADO', 'CONGREGADO'),
        ('DESCONHECIDO', 'DESCONHECIDO')
    ])
    observacao = TextAreaField('De que Igreja e Cidade?', [validators.DataRequired(), validators.Length(min=1, max=200)])
    cadastrar = SubmitField('Cadastrar')

    

class FormularioUsuario(FlaskForm):
    nome = StringField('Nome de usuário', [validators.DataRequired(), validators.Length(min=1, max=8)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    entrar = SubmitField('entrar')

class BuscarMembro(FlaskForm):
    cpf = IntegerField('Buscar membro por CPF', [validators.DataRequired(), validators.Length(max=11)])
    buscar = SubmitField('Buscar')