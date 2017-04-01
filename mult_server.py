import time, _thread as thread
from socket import *

meuHost = ''
minhaPort = 5007
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((meuHost, minhaPort))
sockobj.listen(5)

def lidaCliente(conexao):
	while True:
		data = conexao.recv(1024)
		if not data: break
		conexao.send(b'Eco=> ')

def despacha():
	while True:
		conexao, endereco = sockobj.accept()
		print('Server conectado por', endereco)
		thread.start_new_thread(lidaCliente, (conexao,))

despacha()