'''
    UFG - Instituto de Informática
    Programação Paralela e Distribuída (Prof. Dr. Sérgio Teixeira)
    Aluno: Elton Ricelli F. Rezende
    Implementação simples de CLIENTE e SERVIDOR utilizando IPC e Sockets
'''

import socket, pickle, sys

serverHost = 'localhost'
serverPort = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverHost, serverPort))

dadosFunc = []   
dadosFunc.append(input("Digite o NOME do Funcionário: "))
print("Digite 1 ou 2 para CARGO do FUNCIONÁRIO:")
print("1 - OPERADOR")
print("2 - PROGRAMADOR")
dadosFunc.append(input(""))

if dadosFunc[1] != '1' and dadosFunc[1] != '2':
    print("ESCOLHA SOMENTE OS VALORES 1 ou 2")
    s.close()
    sys.exit()
    
dadosFunc.append(input("Digite o SALÁRIO do Funcionário: "))

try:
    float(dadosFunc[2])
except:
    print("O SALÁRIO DEVE SER UM VALOR NUMÉRICO INTEIRO OU REAL")
    s.close()
    sys.exit()

data_string = pickle.dumps(dadosFunc)
s.send(data_string)

data = s.recv(4096)
DadosFuncAtualizado = pickle.loads(data)
s.close()
print('Received', repr(DadosFuncAtualizado))
