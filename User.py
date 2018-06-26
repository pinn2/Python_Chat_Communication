

import socket
import sys
import time

s=socket.socket()

host = input(str("Enter server name: "))
port = 8080

s.connect((host,port))

print ("Connected to server successfully")

while 1:
        in_msg = s.recv(1024)
        in_msg = in_msg.decode()

        print("Pints: ",in_msg)

        print(" ")

        msg = input(str("You: "))
        msg = msg.encode()
        s.send(msg)
        print ("Deliverd")

        print ("") 
