import time, _thread as thread
from socket import *

def arquivo():
	try:
		arq = open('musica.data', 'r')
	except Exception as e:
		arq = open('musica.data', 'a')
	return arq

def le(arquivo):
	dicionario = {}
	linha = arquivo.readline()
	while linha:
		dicionario[linha.split(':')[0]] = linha.split(':')[1]
		linha = arquivo.readline()
	return dicionario

		
meuHost = ''
minhaPort = 5010
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((meuHost, minhaPort))
sockobj.listen(5)

def busca(data):
	arq = arquivo()
	try:
		return le(arq)[data]
	except Exception as e:
		return 'Nada foi encontrado'

def lidaCliente(conexao):
	while True:
		data = conexao.recv(1024)
		if not data: break
		conexao.send(busca(data.decode()).encode())

def despacha():
	while True:
		conexao, endereco = sockobj.accept()
		print('Server conectado por', endereco)
		thread.start_new_thread(lidaCliente, (conexao,))

despacha()

