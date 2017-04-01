from socket import *

serverHost = 'localhost'
serverPort = 5010

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

linha = input("Informe a mensagem a ser buscada: ")


sockobj.send(linha.encode())

data = sockobj.recv(1024)
print("Cliente recebeu: ", data)

sockobj.close()