from socket import *

serverName = '127.0.0.1'
serverPort = 11111
BUFSIZ = 2048
ADDR = (serverName,serverPort)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(ADDR)

while True:
	returnData = clientSocket.recv(BUFSIZ)
	if not returnData: 
		break
	returnData = returnData.decode('utf-8')
	
	print('received: ',returnData)
	
	str = input('Input what you want to send: ')
	
	clientSocket.send(str.encode('utf-8'))
clientSocket.close()
