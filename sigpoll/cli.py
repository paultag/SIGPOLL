from sigpoll.parser import import_sbs
import outpost

import socket
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def lines(s):
    data = ""
    while True:
        data += s.recv(4096).decode('utf-8')
        if data == "":
            break

        while "\n" in data:
            chunk, data = data.split("\n", 1)
            yield chunk

outpost.sync(host='localhost', port=2017)

for line in lines(s):
    print(import_sbs(line))

s.close()