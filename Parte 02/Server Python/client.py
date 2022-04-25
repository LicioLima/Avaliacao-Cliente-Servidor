from email import message
import socket
import random
from threading import Thread
from datetime import datetime
from tkinter.ttk import separator
from xmlrpc import client
from colorama import Fore, init, back

# cores de inicialização no terminal
init()

# defina as cores disponíveis no padrão
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX]

# escolha uma cor aleatória para o cliente
client.color = random.choice(colors)

# endereço ip do servidor
# se o servidor nao estiver nesta maquina,
# coloque o endereço IP privado(rede) (por exemplo, 192.168.1.2)
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5002 # porta do servidor
seperator_token = '<SEP>' #usaremos isso para separar o nome do cliente

# inicializar soquete TCP
s = socket.socket()
print(f'[*] Connecting to {SERVER_HOST} : {SERVER_PORT}...')
# conectar ao servidor
s.connect((SERVER_HOST, SERVER_PORT))
print('[+] Conectado.')
# solicitar ao cliente um nome
name = input('Digite seu nome: ')

def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print('\n' + message)
t.daemon = True
t.start()

while True:
    to_send = input()
    
    if to_send.lower() == 'q':
        break
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_send = f'(client_color) [{date_now}] {name} {separator_token} {to_send} {Fore.RESET}'
    s.send(to_send.encode())
s.close()