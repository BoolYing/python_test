# -*- coding: utf-8 -*-

import MySQLdb
import datetime
import re
DEBUG = True
 
if DEBUG:
    dbuser = 'root'
    dbpass = '123456'
    dbname = 'bs_db'
    dbhost = '127.0.0.1'
    dbport = '3306'
else:
    dbuser = 'root'
    dbpass = 'lihuipeng'
    dbname = 'game_main'
    dbhost = '127.0.0.1'
    dbport = '3306'
     
class MySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
        #清空表：
        self.cursor.execute("truncate table weather7day;")
        self.conn.commit() 
         
    def process_item(self, item, spider): 
        curTime =  datetime.datetime.now()  
        try:
            self.cursor.execute("""INSERT INTO weather7day (city_code,weatherDate1,weatherDate2, weatherWea, weatherTem1,weatherTem2, weatherWin, updateTime)  
                            VALUES (%s, %s, %s, %s, %s, %s, %s)""", 
                            (
                                item['city_code'],
                                item['weatherDate'][0].encode('utf-8')[:-15],
                                item['weatherDate'][0].encode('utf-8')[-9:-3],
                                item['weatherWea'][0].encode('utf-8'),
                                item['weatherTem1'][0].encode('utf-8'),
								item['weatherTem2'][0].encode('utf-8')[:-3],
                                item['weatherWin'][0].encode('utf-8'),
                                curTime,
                            )
            )
     
            self.conn.commit()
     
     
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item
