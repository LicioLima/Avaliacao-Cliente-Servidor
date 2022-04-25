import socket
from threading import Thread

# Endereço IP do Servidor
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5002 #porta que vamos usar
seperator_token = '<SEP>' # separar o nome do cliente e a mensagem

# inicializaremos todos os soquetes do cliente conectado
cliente_sockets = set()
# criamos um soquete TCP
s = socket.socket()
# porta reutilizável
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# vincular o soquete ao endereçoque especificamos 
s.bind((SERVER_HOST, SERVER_PORT))
# Escutamos as próximas conexões
s.listen(5)
print(f'[*] Ouvindo o {SERVER_HOST} : {SERVER_PORT}')

def listen_for_client(cs):
    '''
    Escutamos as mensagens do soquete do cliente onde 
    a mensagem for recebida transmita-a para todos os outros clientes
    '''
    while True:
        try:
            # continue ouvindo uma mensagem soquete 'cs' que passamos como argumento
            msg = cs.recv(1024).decode()
        except Exception as e:
            # clente nao esta mais conectado
            # vamos remover  do conjunto de lista
            print(f'[!] Error: {e}')
            client_sockets.remove(cs)
        else:
            # se recebemos uma mensagem, substitua o <SEP>
            # token com ":"
            msg = msg.replace(separator_token, ": ")
        for client_socket in client_socket:
            # Enviar mensagem
            client_socket.send(msg.encode())

while True:
    # Continuamos ouvindo novas conexões o tempo todo
    client_socket, client_adress = s.accept()
    print(f'[+] {client_adress} conectado.')
    # adicione o novo cliente conectado aos soquetes conectados
    client_socket.add(client_socket)
    # iniciar um novo thread que escute as mensagens de cada cliente
    t = Thread(target=listen_for_client, args=(client_socket,))
    # terminando sempre que o encadeamento principal terminar
    t.daemon = True
    # iniciar a thread
    t.start()

#fechar os soquetes do cliente
for cs in client_sockets:
    cs.close()
# fechar o soquete do servidor
s.close()