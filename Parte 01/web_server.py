import sys
import cgi
from http.server import HTTPServer, SimpleHTTPRequestHandler  
from database.database import create_table, insert_record, fetch_records

HOST_NAME = 'localhost'
PORT = 8080

def read_html_template(path):
    '''função para ler arquivo html'''
    try:
        with open(path) as f:
            file = f.read()
    except Exception as e:
        file = e
    return file
#############################################################################################

def show_records(self):
    '''função para mostrar registro no modelo'''
    file = read_html_template(self.path)

    #buscar registros no banco de dados
    table_data = fetch_records

    table_row = ' '
    for data in table_data:
        table_row += '<tr>'
        for item in data:
            table_row += '<td>'
            table_row +=  item
            table_row += '</td>'
        table_row += '</tr>'

    #substitua  {{user_records}} no modelo por table_row
    file = file.replace('{{user_records }}', table_row)
    self.send_response(200, 'OK')
    self.end_headers()
    self.wfile.write(bytes(file, 'utf-8'))
#############################################################################################

class PythonServer(SimpleHTTPRequestHandler):
    '''Servidor HTTP Python que lida com solicitações GET e POST'''

    def do_GET(self):
        if self.path == '/':
            self.path = './templates.form.html'
            file = read_html_template(self.path)
            self.send_response(200, 'OK!')
            self.end_headers()
            self.wfile.write(bytes(file, 'utf-8'))

        if self.path == '/show_records':
            self.path = './templates/show_records.html'
            
            #Chame a função show_records para mostrar os usuários inseridos
            show_records(self)

    def do_POST(self):
        if self.path == '/success':

            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                full_name = fields.get('full_name')[0]
                country = fields.get('country')[0]

                #crie a tabela usuário se for executado pela primeira vez, senão não
                create_table()

                #inserir registro na tabela user
                insert_record(full_name, country)

                #obs tudo em única linha
                html = f"<html><head></head><body><h1>Dados do formulário gravados com sucesso!!!</h1><br><a href='/'>Dados Cadastrados</a></body></html>"
                
                self.send_response(200, 'OK!')
                self.end_headers()
                self.wfile.write(bytes(html, 'utf-8'))

                if __name__ == '__main__':
                    server = HTTPServer((HOST_NAME, PORT), PythonServer)
                    print(f"Servidor iniciado http://{HOST_NAME}:{PORT}")

                    try:
                        server.serve_forever()
                    except KeyboardInterrupt:
                        server.server_close()
                        print('Servidor parado com sucesso')
                        sys.exit(0)