# Written by Vamei
# Client side
import socket

# Address
host = '127.0.0.1'
port = 8955

request = 'please give me the user_info?'

# configure socket
s       = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# send message
s.send(request)
# receive message
reply   = s.recv(1024)
print 'reply is: ',reply
# close connection
s.close()

