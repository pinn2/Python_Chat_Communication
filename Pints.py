


import socket
import sys
import time


s=socket.socket()              # socket variable
host = socket.gethostname()    # getting host name of server
print (host)

port =8080                     # use server 8080 port number for communication
s.bind((host,port))            # port binded with host to communication
print ("Successfully connected host and port")

s.listen(1)                    # waiting for 1 number of user to communicate
print ("Pints waiting for connection")

print (" ")
 
conn,add = s.accept()          # if any user connect then it accept connection request return the connection obj->conn and
                               # add contain host name of user as I.P address and port number
print (add,"Has connected to Pints")

print (" ")
while 1:
        msg = input(str("Pints: "))   # server Pints message to send
        msg = msg.encode()            # message encoded into bit frame
        conn.send(msg)                # message send  to user
        print ("Deliverd")
        print (" ")


        in_msg = conn.recv(1024)      # message recieved by user
        in_msg = in_msg.decode()      # decode to print String message

        print("User: ",in_msg)
        print (" ")
