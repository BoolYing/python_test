# -*- coding: utf-8 -*-
import socket

obj = socket.socket()
obj.connect(('127.0.0.1', 8001))

while True:
    inp = input('>>>')
    obj.sendall(inp)
    ret = obj.recv(1024)
    print(ret)

obj.close()
