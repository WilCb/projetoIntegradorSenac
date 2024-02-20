SECRET_KEY = 'alakazan'

SQLALCHEMY_DATABASE_URI = \
    'postgresql+psycopg2://{usuario}:{senha}@{servidor}/{database}'.format(
        usuario='postgres',
        senha='1234',
        servidor='localhost',
        database='igreja'
    )
