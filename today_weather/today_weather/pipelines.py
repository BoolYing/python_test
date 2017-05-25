# -*- coding: utf-8 -*-

import MySQLdb
import datetime
import re
from settings import dbuser,dbpass,dbname,dbhost,dbport


class MySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
        #清空表：
        self.cursor.execute("truncate table weather7day_full;")
        self.conn.commit() 
    def process_item(self, item, spider):
        curTime =  datetime.datetime.now()
        try:
            self.cursor.execute("""INSERT INTO weather7day_full (city_code,weatherDate, weatherWea, weatherTem, weatherWinf,weatherWinl, updateTime)  
                            VALUES (%s, %s, %s, %s, %s, %s, %s)""", 
                            (
                                item['city_code'],
                                item['content'].split(',')[0],
                                item['content'].split(',')[2],
                                item['content'].split(',')[3],
                                item['content'].split(',')[4],
                                item['content'].split(',')[5], #五和六
                                curTime,
                            )
            )
            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item







'''
        contents = item["content"][0].encode('utf-8')
        print(contents) 
        item_list = re.findall(r'"(.*?)"', contents)
        #调试：输出全部信息：1d --23d --7d --结束
        for x in item_list:
            print(x)
        i = item_list.index("1d") 
        j = item_list.index("23d")
        oneday = item_list[i+1:j]
        #调试：输出24小时内的天气：1d --23d
        print("1d -- 23d:")
        for x in oneday:
            print(x)
            x=x.split(',')
            #开始插入数据库
            #x[0]---x[6]
'''                    
