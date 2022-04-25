from sqlite3 import connect
from sqlite3.dbapi2 import Cursor
DB_NAME = "database/user_records.db" #nome da base de dados
#crie banco de dados dentro da pasta do banco de dados se não existir
connection = connect(DB_NAME)
cursor = connection.cursor()
def create_table():
    '''função para criar tabela dentro do banco de dados'''
    table_script = '''CREATE TABLE IF NOT EXISTS User(
                    full_name VARCHAR(255),
                    country VARCHAR (150);'''
    cursor.executescript(table_script)
    connection.commit()
    def insert_record(fullname, country):
        '''função para inserir registro dentro da tabela'''
        cursor.execute('INSERT INTO User(full_name, country) values(?, ?)',
                       (fullname, country))
        connection.commit()
    def fetch_records():
        '''função para buscar registros do usuário'''
        data = cursor.execute('SELECT * FROM User')
        return data