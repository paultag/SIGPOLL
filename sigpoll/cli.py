from sigpoll.parser import import_sbs
import outpost

from django.conf import settings
import django

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((settings.SBS_SERVER, settings.SBS_PORT))

def lines(s):
    data = ""
    while True:
        data += s.recv(4096).decode('utf-8')
        if data == "":
            break

        while "\n" in data:
            chunk, data = data.split("\n", 1)
            yield chunk

def daemon():
    django.setup()
    if settings.OUTPOST_ENABLE:
        outpost.sync(host=settings.OUTPOST_SERVER, port=settings.OUTPOST_PORT)

    for line in lines(s):
        print("Loaded: ", *import_sbs(line, dedupe=True))
    s.close()
