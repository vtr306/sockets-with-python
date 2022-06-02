import socket
from _thread import *

serverPort = 8080
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clients = []

try:
    serverSocket.bind(('localhost', serverPort))
except socket.error as e:
    print(str(e))

print('Waiting for connection ...')
serverSocket.listen()

def threaded_client(connection):
    while True:
        data = connection.recv(2048)
        if not data:
            break
        for client in clients:
            if client != connection:
                client.send(data)
    connection.close()

while True:
    connectionSocket, addr = serverSocket.accept()
    print('Conection established with: ' + addr[0] + ':' + str(addr[1]))
    start_new_thread(threaded_client, (connectionSocket, ))
    clients.append(connectionSocket)

connectionSocket.close()