# Written by Vamei
# Server side
import socket
import MySQLdb

# Mysql
dbuser = 'root'
dbpass = '123456'
dbname = 'bs_db'
dbhost = '127.0.0.1'
dbport = '3306'
conn=MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset="utf8", use_unicode=True)
cur=conn.cursor()

# Address
HOST = ""
PORT = 8955


# Configure socket
s      = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
s.bind((HOST, PORT))

# passively wait, 3: maximum number of connections in the queue
s.listen(3)
# accept and establish connection
while 1:
    conn, addr = s.accept()
    request    = conn.recv(1024)
    print 'request is: ',request
    print 'Connected by', addr
    cur.execute('select * from user_info;')
    results = cur.fetchall()
    result = list(results)
    reply = []
    for r in result:
        reply.append((r.)
        


    
    conn.sendall(reply)
    conn.close()



