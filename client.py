from socket import *

serverHost = 'localhost'
serverPort = 5007

mensagem = [b'Ola mundo']

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

for linha in mensagem:
	sockobj.send(linha)

	data = sockobj.recv(1024)
	print("Cliente recebeu: ", data)

sockobj.close()