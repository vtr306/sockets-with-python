import socket
from _thread import *

serverPort = 8080

try:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print("Create socket failed: %s" % e)
    sys.exit(1)

try:
    clientSocket.connect(('localhost', serverPort))
except socket.gaierror as e:
    print("Address-related error: %s" % e)
    sys.exit(1)
except socket.error as e:
    print("Error connecting to server: %s" % e)
    sys.exit(1)

print("Server Connection Accepted")

user = input("Insert username: ")

def receiveMessage(connection):
    while True:
        sentence = input()
        try:
            connection.send((f'<{user}> {sentence}').encode('utf-8'))
        except socket.error as e:
            print("Error sending data: %s" % e)

def sendMessage(connection):
    while True:
        try:
            serverSentence = connection.recv(2048)
            serverSentence = serverSentence.decode('utf-8')
            print(serverSentence)
        except socket.error as e:
            print("Error receiving data: %s" % e)

start_new_thread(sendMessage, (clientSocket, ))
start_new_thread(receiveMessage, (clientSocket, ))

while True:
    pass

clientSocket.close()
print("Server Connection closed")