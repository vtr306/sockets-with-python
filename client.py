import socket
from _thread import *

serverPort = 8080
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('localhost', serverPort))
print("Server Connection Accepted")

user = input("Insert username: ")

def receiveMessage(connection):
    while True:
        sentence = input()
        connection.send((f'<{user}> {sentence}').encode('utf-8'))

def sendMessage(connection):
    while True:
        serverSentence = connection.recv(2048)
        serverSentence = serverSentence.decode('utf-8')
        print(serverSentence)

start_new_thread(sendMessage, (clientSocket, ))
start_new_thread(receiveMessage, (clientSocket, ))

while True:
    pass

clientSocket.close()
print("Server Connection closed")