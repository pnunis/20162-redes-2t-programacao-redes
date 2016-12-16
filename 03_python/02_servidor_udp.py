import socket
serverHost = socket.gethostbyname('localhost')
serverPort = 12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSocket.bind((serverHost, serverPort))

print('O servidor está pronto para receber:')
#print('Conexão de:', addr)

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    #processa a string para letras maiúsculas
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)