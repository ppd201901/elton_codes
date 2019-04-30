import socket
import sys
from _thread import *

host = "localhost"
port = 12345


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("socket criado")

try:
    s.bind((host, port))
except socket.error:
    print("Conexão FALHOU")
    sys.exit()
print("Socket conectado")

s.listen(10)
print("Socket PRONTO")

def clientthread(conn):
    msgBoasVindas = "CONECTADO ao Servidor!!!\n"
    conn.send(msgBoasVindas.encode())

    # conexão e criação da THREAD com cada CLIENTE (Armazenamento do nome do RESPECTIVO CLIENTE)
    data = conn.recv(1024)
    nome = data.decode()
    print("Conectado com: " + addr[0] + ": " + str(addr[1]))

    while True:
        data = conn.recv(1024)
        mensagem = nome + ": " + data.decode()
        # reply = nome + "CLIENTE:" + data.decode()

        if not data:
            break;
        print(mensagem)

        # SERVIDOR REENVIA MENSAGEM PARA TODOS???
        #conn.sendall(data)

    conn.close()

while 1:
    conn, addr = s.accept()
    start_new_thread(clientthread, (conn,))


conn, addr = s.accept()
print("Conectado com" + addr[0] + ":" + str(addr[1]))

s.close()

'''
while 1:
    data = conn.recv(1024)
    print("CLIENTE: " + data.decode())
    if not data:
        break;
    # conn.sendall(data)
    # conn.sendall(data.decode())
'''