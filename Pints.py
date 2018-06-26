


import socket
import sys
import time


s=socket.socket()
host = socket.gethostname()
print (host)

port =8080
s.bind((host,port))
print ("Successfully connected host and port")

s.listen(1)
print ("Pints waiting for connection")

print (" ")

conn,add = s.accept()
print (add,"Has connected to Pints")

print (" ")
while 1:
        msg = input(str("Pints: "))
        msg = msg.encode()
        conn.send(msg)
        print ("Deliverd")
        print (" ")


        in_msg = conn.recv(1024)
        in_msg = in_msg.decode()

        print("User: ",in_msg)
        print (" ")
