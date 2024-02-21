from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import StringField, PasswordField, SubmitField, validators, SelectField, IntegerField, DateField, TelField, TextAreaField, ValidationError

from config import sexo_lista, uf_lista, estado_civil_lista, escolaridade_lista, confirm_lista, funcao_lista, origem_lista, situacao_lista

class FormularioCadastro(FlaskForm):
    nome = StringField('Nome', [validators.DataRequired(), validators.Length(min=3, max=70)])
    rg = IntegerField('RG', [validators.DataRequired()])
    cpf = StringField('CPF', [validators.DataRequired(), validators.Length(max=11)])
    orgao_expedidor = StringField('Orgão Expedidor', [validators.DataRequired(), validators.Length(min=3, max=20)])
    sexo = SelectField('Função', [validators.DataRequired()], choices=sexo_lista(), default='')
    pai = StringField('Pai', [validators.DataRequired(), validators.Length(min=3, max=70)])
    mae = StringField('Mãe', [validators.DataRequired(), validators.Length(min=3, max=70)])
    naturalidade = StringField('Naturalidade', [validators.DataRequired(), validators.Length(min=3, max=70)])
    ufIdentidade = SelectField('UF Identidade', [validators.DataRequired()], choices=uf_lista(), default='')
    pais = StringField('País', [validators.DataRequired(), validators.Length(min=2, max=50)])
    cep = IntegerField('CEP', [validators.DataRequired()])
    logradouro = StringField('Logradouro', [validators.DataRequired(), validators.Length(min=1, max=100)])
    numero = IntegerField('N: ', [validators.DataRequired()])
    complemento = StringField('Complemento', [validators.Length(max=100)])
    bairro = StringField('Bairro', [validators.DataRequired(), validators.Length(min=1, max=100)])
    cidade = StringField('Cidade', [validators.DataRequired(), validators.Length(min=1, max=50)])
    ufEndereco = SelectField('UF', [validators.DataRequired()], choices=uf_lista(), default='')
    telefone = TelField('Telefone', [validators.DataRequired(), validators.Length(min=1, max=13)])
    dataNascimento = DateField('Data de Nascimento', [validators.DataRequired()])
    estadoCivil = SelectField('Estado Civil', [validators.DataRequired()], choices=estado_civil_lista(), default='')
    nomeConjuge = StringField('Nome do Cônjuge', [validators.Length(min=1, max=70)])
    profissao = StringField('Profissão', [validators.DataRequired(), validators.Length(min=1, max=50)])
    escolaridade = SelectField('Escolaridade', [validators.DataRequired()], choices=escolaridade_lista(), default='')
    dataDeBatismo = DateField('Data de batismo')
    batizado = SelectField('Batizado no Espírito Santo?', [validators.DataRequired()], choices=confirm_lista(), default='')
    entradaRol = DateField('Entrada no ROL')
    congregacao = IntegerField('Congregação', [validators.DataRequired()])
    funcao = SelectField('Função', [validators.DataRequired()], choices=funcao_lista(), default='')
    origem = SelectField('Origem', [validators.DataRequired()], choices=origem_lista(), default='')
    situacao = SelectField('Situação', [validators.DataRequired()], choices=situacao_lista(), default='')
    observacao = TextAreaField('De que Igreja e Cidade?', [validators.DataRequired(), validators.Length(min=1, max=200)])
    cadastrar = SubmitField('Cadastrar')
    buscar = SubmitField('Buscar')

    

class FormularioUsuario(FlaskForm):
    nome = StringField('Nome de usuário', [validators.DataRequired(), validators.Length(min=1, max=8)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    entrar = SubmitField('entrar')

