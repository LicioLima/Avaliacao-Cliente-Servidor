import socket
import tqdm
import os
import argparse

SEPERATOR = "<SEPARATOR>"

BUFFER_SIZE = 1024 * 4

def send_file(filename, host, port):
    filesize = os.path.getsize(filename)
    s = socket.socket
    print(f"[+] Conectando ao servidor {host}:{port}")
    s.connect((host, port))
    print("[+] Conectando.")

    # envie o nome do arquivo e o tamanho do arquivo
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    # enviar o arquivo

    progress = tqdm.tqdm(range(filesize), f"Enviando {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            #leitura dos bytes do arquivo
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
             break
        #usamos o sendall para garantir a transmissão em
        # redes ocupadas
        s.sendall(bytes_read)
        #atualizar barra de progresso
        progress.update(len(bytes_read))
#fechando socket
    s.close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Simple File Sender")
    parser.add_argument("file", help="File name to send")
    parser.add_argument("host", help="The host/IP address the receiver")
    parser.add_argument("-p", "--port", help="Port to use, default is 5001", type=int, default=5001)
    args = parser.parse_args()
    filename = args.file
    host = args.host
    port = args.port
    send_file(filename, host, port)