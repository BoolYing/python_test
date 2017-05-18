# -*- coding: utf-8 -*-
import scrapy
from ..items import WeatherItem 
import re
from scrapy.selector import Selector
import urllib2,time
import MySQLdb


DEBUG = True

if DEBUG:
    dbuser = 'root'
    dbpass = '123456'
    dbname = 'bs_db'
    dbhost = '127.0.0.1'
    dbport = '3306'
else:
    dbuser = 'root'
    dbpass = '123456'
    dbname = 'bs_db'
    dbhost = '192.168.1.101'
    dbport = '3306'

def get_urls():
    try:
        conn=MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset="utf8", use_unicode=True)
        cur=conn.cursor()
        cur.execute('select * from register_city;')
        s=[]
        results = cur.fetchall()
        result=list(results)
        for r in result:
            #将数据库中的城市代码列表，构建成url列表的形式，并返回url列表
            s.append(("http://www.weather.com.cn/weather1d/%s.shtml" % r))
        conn.close()
        return s
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

 
class CatchWeatherSpider(scrapy.Spider):
    name = 'CatchWeather'
    allowed_domains = ['weather.com.cn']
    #start_urls = [ "http://www.weather.com.cn/weather/101280101.shtml" ]
    start_urls = get_urls()
     
    def parse(self, response):

        #从网页源码中获取城市代码，用来分辨天气记录是属于哪一个城市的
        city_code_path = sel.xpath('//*[@id="someDayNav"]/li[1]/a/@href').extract()
        city_code_path = city_code_path[0].encode('utf-8')
        #city_code_path 的形式是："/weather1d/101110102.shtml"，需要用正则表达式提取city_code
        city_code = re.findall(r'/weather1d/(.+?).shtml',city_code_path)[0]

        for sel in response.xpath('//*[@id="7d"]/ul/li'):
            item = WeatherItem()
            item["city_code"] = city_code
            item['weatherDate'] = sel.xpath('h1/text()').extract() 
            #item['weatherWea'] = sel.xpath('p[@class="wea"]/text()').extract()
            #print(response.xpath('//*[@id="around"]/div[1]/ul/li[1]/a/span/text()').extract())
            #print(response.xpath('//*[@id="curve"]/div[1]/em[1]/text()').extract())
            item['weatherWea'] = sel.xpath('p[1]/text()').extract()
            item['weatherTem1'] = sel.xpath('p[@class="tem"]/span/text()').extract()
            item['weatherTem2'] = sel.xpath('p[@class="tem"]/i/text()').extract()
            item['weatherWin'] = sel.xpath('p[@class="win"]/i/text()').extract()
            yield item

