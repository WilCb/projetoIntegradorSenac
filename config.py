SECRET_KEY = 'alakazan'

SQLALCHEMY_DATABASE_URI = \
    'postgresql+psycopg2://{usuario}:{senha}@{servidor}/{database}'.format(
        usuario='postgres',
        senha='1234',
        servidor='localhost',
        database='igreja'
    )

def sexo_lista():
    return [
        ('', 'Selecione'),
        ('MASCULINO', 'MASCULINO'),
        ('FEMININO', 'FEMININO')
    ]

def uf_lista():
    return [
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
    ]

def estado_civil_lista():
    return [
        ('', 'Selecione'),
        ('Solteiro', 'Solteiro'),
        ('Casado', 'Casado'),
        ('Divorciado', 'Divorciado'),
        ('Viúvo', 'Viúvo'),
        ('Separado Judicialmente', 'Sep. Judicialmente')
    ]

def escolaridade_lista():
    return [
        ('', 'Selecione'),
        ('Analfabeto', 'Analfabeto'),
        ('Alfabetizado', 'Alfabetizado'),
        ('Primário', 'Primário'),
        ('1° Grau', '1° Grau'),
        ('2° Grau', '2° Grau'),
        ('Superior', 'Superior')
    ]

def confirm_lista():
    return [
        ('', 'Selecione'),
        ('SIM', 'SIM'),
        ('NÃO', 'NÃO')
    ]

def funcao_lista():
    return [
        ('', 'Selecione'),
        ('PASTOR', 'PASTOR'),
        ('EVANGELISTA', 'EVANGELISTA'),
        ('PRESBÍTERIO', 'PRESBÍTERIO'),
        ('DIÁCONO', 'DIÁCONO'),
        ('AUXILIAR', 'AUXILIAR'),
        ('MEMBRO', 'MEMBRO')
    ]

def origem_lista():
    return [
        ('', 'Selecione'),
        ('BATISMO', 'BATISMO'),
        ('TRANFERÊNCIA', 'TRANFERÊNCIA'),
        ('PRESBÍTERIO', 'PRESBÍTERIO'),
        ('ACLAMAÇÃO', 'ACLAMAÇÃO'),
        ('CONGREGAÇÃO', 'CONGREGAÇÃO')
    ]

def situacao_lista():
    return [
        ('', 'Selecione'),
        ('ATIVO', 'ATIVO'),
        ('DISCIPLINADO', 'DISCIPLINADO'),
        ('TRANSFERIDO', 'TRANSFERIDO'),
        ('FALECIDO', 'FALECIDO'),
        ('CAND. BATISMO', 'CAND. BATISMO'),
        ('DESVIADO', 'DESVIADO'),
        ('CONGREGADO', 'CONGREGADO'),
        ('DESCONHECIDO', 'DESCONHECIDO')
    ]