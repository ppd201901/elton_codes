'''
    UFG - Instituto de Informática
    Programação Paralela e Distribuída (Prof. Dr. Sérgio Teixeira)
    Aluno: Elton Ricelli F. Rezende
    Implementação simples de CLIENTE e SERVIDOR utilizando IPC e Sockets
'''

import socket, pickle

serverHost = 'localhost'
serverPort = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((serverHost, serverPort))
s.listen(1)
conn, addr = s.accept()

#CONFIRMAÇÃO DA CONEXÃO FEITA
print('Connected by', addr)

while True:
    data = conn.recv(4096)
    if not data: break

    dadosFunc = []
    dadosFunc = pickle.loads(data)
    dadosFunc[1] = int(dadosFunc[1])
    dadosFunc[2] = float(dadosFunc[2])
    
    if dadosFunc[1] == 1:
        dadosFunc[2] = dadosFunc[2] + (dadosFunc[2] * 0.20)
    elif dadosFunc[1] == 2:
        dadosFunc[2] = dadosFunc[2] + (dadosFunc[2] * 0.18)

    print(dadosFunc)
    
    data_string = pickle.dumps(dadosFunc)
    conn.send(data_string)    
    
conn.close()
