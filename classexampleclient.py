# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:25:50 2020

@author: blattj
"""

import socket
serverIP = '10.220.89.73'
Port = 9999
sentence = input('Input lowercase sentence:')
while (sentence != 'exit'):
    Clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Clientsocket.connect((serverIP,Port))
    Clientsocket.send(sentence.encode())
    modifiedSentence = Clientsocket.recv(1024)
    print('From Server: ', modifiedSentence.decode())
    Clientsocket.close()
    sentence = input('Input lowercase sentence:')