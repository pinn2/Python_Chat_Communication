

import socket
import sys
import time

s=socket.socket()

# server name for connecting to server

host = input(str("Enter server name: "))

# port number on which user want to connect

port = 8080

# making socket (hostname+port number) and connection

s.connect((host,port))

print ("Connected to server successfully")

while 1:
        in_msg = s.recv(1024)       # user recieve message from server and buffer size is 1024 which shows max length of message in bit form
        in_msg = in_msg.decode()    # input bit string decoded into the valid string

        print("Pints: ",in_msg)     # show Recieved message

        print(" ")

        msg = input(str("You: "))  # user message
        msg = msg.encode()         # user message encoded for transmission
        s.send(msg)                # send user message to server
        print ("Deliverd")

        print ("") 
