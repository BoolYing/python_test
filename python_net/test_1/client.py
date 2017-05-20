# -*- coding: utf-8 -*-
# Written by Vamei
# Client side
import socket
import sys
# Address
host = '127.0.0.1'
port = 8955

def useage():
    print('\n\t\targuement:\n\t\t 1:user_info\n\t\t 2:user_login\n\t\t 3:weather7day\n\t\t 4:weather7day_full\n')


if sys.argv[1] == '1':
    request = 'user_info'
elif sys.argv[1] == '2':
    request = 'user_login'
elif sys.argv[1] == '3':
    request = 'weather7day'
elif sys.argv[1] == '4':
    request = 'weather7day_full'
elif sys.argv[1] == '-h':
    useage()
    sys.exit()
else:
    print("%s:非法参数" % sys.argv[1])
    sys.exit()




# configure socket
s       = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# send message
s.send(request)
# receive message]
reply   = s.recv(10000000)
print "reply  is:\n",reply
print "reply length is :",len(reply)
# close connection
s.close()

