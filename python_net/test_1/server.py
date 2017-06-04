# -*- coding: utf-8 -*-
# Written by Vamei
# Server side
import socket   
import MySQLdb
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
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

def select_query(query):
    connect = None
    try:
        connect=MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset="utf8", use_unicode=True)
        cur=connect.cursor()
        cur.execute(query)
        results = cur.fetchall()
        if connect:
            cur.close()
            connect.close()
        return results
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit()

def select_user_info(username):
    print username
    query = 'select city  from user_info where username = "%s"' % username
    print query
    results = select_query(query)
    result = list(results)
    reply = ''
    for r in result:
        reply += r[0]
        reply += ','
    return reply

def select_user_login(login_info):
    reply = "no"
    print login_info
    username = login_info.split(',')[0]
    password = login_info.split(',')[1]
    query = 'select password from user_login where username="%s";'% username
    print query
    results = select_query(query)
    if(results):
        passwd = list( list(results)[0])[0]
        if passwd == password:
            reply = 'yes'
    return reply


#cur.execute('select id,city_code,weatherDate1,weatherDate2,weatherWea,weatherTem1,weatherTem2,weatherWin,updateTime from weather7day;')

def select_weather7day(username):
    print username
    query = 'select * from weather7day where city_code in (select city from user_info where username = "%s") order by cast(city_code as unsigned),id asc'% username
    print query
    results = select_query(query)
    result = list(results)
    reply = ''
    for r in result:
        #reply += r[0]
        #reply += ','
        reply += r[1]
        reply += ','
        reply += r[2]
        reply += ','
        reply += r[3]
        reply += ','
        reply += r[4]
        reply += ','
        reply += r[5]
        reply += ','
        reply += r[6]
        reply += ','
        reply += r[7]
        reply += ';'
        #reply += r[8]
        #reply += ';'
    return reply 


#cur.execute('select id,city_code,weatherDate,weatherWea,weatherTem,weatherWinf,weatherWinl,updateTime from weather7day_full;')
def select_weather7day_full(username):
    print username
    query = 'select * from weather7day_full where city_code in (select city from user_info where username = "%s") order by cast(city_code as unsigned),id asc'% username
    print query
    results = select_query(query)
    result = list(results)
    reply = ''
    for r in list(result):
        #reply += `r[0]` + ','
        reply += r[1] + ','
        reply += r[2] + ','
        reply += r[3] + ','
        reply += r[4] + ','
        reply += r[5] + ','
        reply += r[6] + ';'
        #reply += `r[7]` + ';'
    print reply
    return reply 

def select_city_code():
    query = 'select * from city_code'
    results = select_query(query)
    result = list(results)
    reply = ''
    for r in list(result):
        reply += r[0] + ','
        reply += r[1] + ','
        reply += r[2] + ','
        reply += r[3] + ';'
    print reply
    return reply

    


'''
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
    request    = conn.recv(1)
    print 'request is: ',request
    print 'Connected by', addr
    reply=' '
    if request == '2':#用户关注城市代码列表
        username = conn.recv(1024)
        reply = select_user_info(username)
    elif request == '1':#用户登录验证
        login_info = conn.recv(1024)
        reply = select_user_login(login_info)
    elif request == '3':#未来七天大致天气
        username = conn.recv(1024)
        reply = select_weather7day(username)
    elif request == '4':#未来七天详细信息
        username = conn.recv(1024)
        reply = select_weather7day_full(username)
    elif request == '5':#请求城市代码
        reply = select_city_code()
    else:
        print("客户端请求的参数错误，不在预期范围内。") 
    conn.sendall(reply.encode('utf-8'))
    conn.close()

