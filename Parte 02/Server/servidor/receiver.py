import socket
import tqdm
import os

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001

BUFFER_SIZE = 4096

SEPERATOR = "<SEPARATOR>"
#cria o socket do servidor
#Socket TCP
s = socket.socket()
#vincular o soquete ao nosso endereço local
s.bind((SERVER_HOST, SERVER_PORT))
#habilitando nosso servidor a aceitar as conexões
#5 aqui é o número de conexões não aceitas que
#o sistema permitirá antes de recusar novas conexões
s.listen(5)
print(f"[*] ouvindo no servidor {SERVER_HOST}:{SERVER_PORT}")
#aceitar conexão se houver alguma
client_socket, address = s.accept()
#se o código abaixo for executado, isso significa que o remetente está com
print(f"[+]{address} esta conectado.")
#recebe as informações do arquivo
#recebe usando o socket do cliente, não o socket do servidor
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPERATOR)
#remova o caminho absoluto se houver
filename = os.path.basename(filename)
#converter para inteiro
filesize = int(filesize)
#começa a receber o arquivo do socket
#e gravando no fluxo do arquivo
progress = tqdm.tqdm(range(filesize), f"Recebendo {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open (filename, "wb") as f:
    while True:
        # ler 1024 bytes do soquete (receber)
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            # se a não for recebido
            # a transmissão do arquivo é feita
            break
        # escreva no arquivo os bytes
        f.write(bytes_read)
        #atualizar a barra de progresso
        progress.update(len(bytes_read))
# feche o soquete cliente
client_socket.close()
# feche o soquete do servidor
s.close()