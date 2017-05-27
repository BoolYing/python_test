# Written by Vamei
# Server side
import socket   
import MySQLdb
import sys
import select
# Mysql
dbuser = 'root'
dbpass = '123456'
dbname = 'bs_db'
dbhost = '127.0.0.1'
dbport = '3306'

# Address
HOST = ""
PORT = 8955


def select_user_info():
    connect = None
    try:
        connect=MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset="utf8", use_unicode=True)
        cur=connect.cursor()
        cur.execute('select username,city from user_info;')
        results = cur.fetchall()
        result = list(results)
        reply = ''
        for r in result:
            reply += '['
            reply += r[0]
            reply += ','
            reply += r[1]
            reply += '];'

        if connect:
            cur.close()
            connect.close()
        return reply
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit()

def select_user_login():
    connect = None
    try:
        connect=MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset="utf8", use_unicode=True)
        cur=connect.cursor()
        cur.execute('select username,password from user_login;')
        results = cur.fetchall()
        result = list(results)
        reply = ' '
        for r in result:
            reply += '['
            reply += r[0]
            reply += ','
            reply += r[1]
            reply += '];'
        if connect:
            cur.close()
            connect.close()
        return reply
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit()

#cur.execute('select id,city_code,weatherDate1,weatherDate2,weatherWea,weatherTem1,weatherTem2,weatherWin,updateTime from weather7day;')

def select_weather7day():
    f = None
    try:
        f = open('/var/lib/mysql-files/weather7day.txt')
        print('weather7day_full.txt is opened')
        reply = f.read()
        print("file content:\n%s"%reply)
        return reply
    except Exception as err:
        print("File operation failed:" + str(err))
        return ' '
    finally:
        if f:
            f.close()
            print('weather7day_full.txt is closed')


#cur.execute('select id,city_code,weatherDate,weatherWea,weatherTem,weatherWinf,weatherWinl,updateTime from weather7day_full;')
def select_weather7day_full():
    f = None
    try:
        f = open('/var/lib/mysql-files/weather7day_full.txt')
        print('weather7day_full.txt is opened')
        reply = f.read()
        print("file content:\n%s"%reply)
        return reply
    except Exception as err:
        print("File operation failed:" + str(err))
        return ' '
    finally:
        if f:
            f.close()
            print('weather7day_full.txt is closed')

    pass


# Configure socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
s.bind((HOST, PORT))
s.listen(1024)

r_list = [s,]
num = 0
# accept and establish connection
while True:
    rl,wl,error = select.select(r_list, [], [])
    num += 1
    print('--------counts is %s'%num)
    print("--------rl's length is %s"%len(rl))
    for fd in rl:
        if fd == s:
            conn, addr = fd.accept()
            r_list.append(conn)
            request = conn.recv(1024)  
            print 'Connected by', addr
            print request
            reply = "connect to server succeed!"
            conn.sendall(reply)
        else:
            try:
                request = conn.recv(1024)
                print 'requests: ',request
                if request == 'user_info':
                    reply = select_user_info()
                elif request == 'user_login':
                    reply = select_user_login()
                elif request == 'weather7day':
                     reply = select_weather7day()
                elif request == 'weather7day_full':
                     reply = select_weather7day_full()
                conn.sendall(reply)

                #fd.sendall('second ...,,,,;;;')
            except ConnectionAbortedError:
                r_list.remove(fd)
                #sys.exit()
    conn.close()
'''
# Configure socket
s      = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((HOST, PORT))

# passively wait, 3: maximum number of connections in the queue
s.listen(1024)
# accept and establish connection
while 1:
    conn, addr = s.accept()
    request    = conn.recv(1024)
    print 'request is: ',request
    print 'Connected by', addr

    if request == 'user_info':
        reply = select_user_info()
    elif request == 'user_login':
        reply = select_user_login()
    elif request == 'weather7day':
        reply = select_weather7day()
    elif request == 'weather7day_full':
        reply = select_weather7day_full()
    #reply = '----ok,here is all info you need----\n'
    conn.sendall(reply)
    conn.close()
'''
