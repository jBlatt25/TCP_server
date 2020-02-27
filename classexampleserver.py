# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:20:00 2020

@author: blattj
"""
import socket
serverPort = 9999

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('server is ready to recieve')
while True:
    connectionSocket, addr = serverSocket.accept()
    print('Connected with' + addr[0] + ':' + str(addr[1]))
    sentence = connectionSocket.recv(1024).decode()
    if (sentence == 'one'):
        sendback = '1'
        connectionSocket.send(sendback.encode())
        break
    captializedSentence = sentence.upper()
    connectionSocket.send(captializedSentence.encode())
    connectionSocket.close