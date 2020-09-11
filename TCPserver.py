from socket import *
import types

port = 11111
host = ''
ADDR = (host, port)
BUFSIZ = 2048

tcpSocket = socket(AF_INET, SOCK_STREAM)
tcpSocket.bind(ADDR)
tcpSocket.listen(5)

while True:
    print('waiting for connection...')
    clientSocket, clientAddr = tcpSocket.accept()
    print('conneted from: %s' %clientAddr[0])
    
    clientSocket.send('connected succefully'.encode('utf-8'))

    while True:
        try:
            data = clientSocket.recv(BUFSIZ)
        except IOError as e:
            print(e)
            clientSocket.close()
            break
        if not data:
            break
            
        returnData = data.decode('utf-8')
        
        print('receive: ',returnData)
        
        str = input('Input what you want to send: ')
        
        clientSocket.send(str.encode('utf-8'))
    clientSocket.close()
tcpSocket.close()
