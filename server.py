import socket
from _thread import *
import sys

serverPort = 8080
try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print("Create socket failed: %s" % e)
    sys.exit(1)

clients = []

try:
    serverSocket.bind(('localhost', serverPort))
except socket.error as e:
    print("Error binding socket to the port: %s" %e )
    sys.exit(1)

print('Waiting for connection ...')
serverSocket.listen()

def threaded_client(connection):
    while True:
        try:
            data = connection.recv(2048)
        except socket.error as e:
            print("Error receiving data: %s" % e)
            break
        if not data:
            break
        for client in clients:
            if client != connection:
                try:
                    client.send(data)
                except socket.error as e:
                    print("Error sending data: %s" % e)
    connection.close()

while True:
    try:
        connectionSocket, addr = serverSocket.accept()
        print('Conection established with: ' + addr[0] + ':' + str(addr[1]))
        start_new_thread(threaded_client, (connectionSocket, ))
        clients.append(connectionSocket)
    except socket.error as e:
        print("Error Establishing connection: %s" % e)

connectionSocket.close()