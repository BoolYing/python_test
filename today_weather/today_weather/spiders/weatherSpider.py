import scrapy
from ..items import TodayWeatherItem
import re
from scrapy.selector import Selector
import urllib2,time
class CatchWeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ['weather.com.cn']
    start_urls = [
        "http://www.weather.com.cn/weather1d/101280101.shtml"
    ]
     
    def parse(self, response):
        sel=Selector(response)
        #sites=sel.xpath('//*[@id="today"]/script/text()').extract() 
        #print('test--1:%s' % sites)
        item = TodayWeatherItem()
        contents = sel.xpath('//*[@id="today"]/script/text()').extract()
        contents = contents[0].encode('utf-8')
        item_list = re.findall(r'"(.*?)"', contents)
        i = item_list.index("7d")
        for x in item_list[i+1:]:
            item = TodayWeatherItem()
            item["content"] = x 
            yield item














 
        
                


        #sel = response.xpath('//*[@id="today"]/div/div[@class="curve_livezs"]')
        #for i in [1,2,3,4,5,6,7,8]:
            #print("test--1:%s" % response.xpath('//*[@id="around"]/div[1]/ul/li[2]/a/span/text()').extract())
            #print('test--2:%s' % response.xpath('/html/body/div[@class="con today clearfix"]/div[@class="left fl"]/div[@class="today clearfix"]/div[@class="curve_livezs"]/div[@class="time"]/em[@style="width:85px;left:0px"]/text()').extract())
            #print('test--2:%s' % sel.xpath('div[@class="time"]/em[@style][1]/text()').extract())
            #item = TodayWeatherItem()
            #item['weatherTime'] = response.xpath('//*[@id="curve"]/div[1]/em[%d]/text()' % i).extract()
            #item['weatherTem']  = response.xpath('//*[@id="curve"]/div[4]/em[%d]/text()' % i).extract()
            #item['weatherWinf'] = response.xpath('//*[@id="curve"]/div[5]/em[%d]/text()' % i).extract()
            #item['weatherWinl'] = response.xpath('//*[@id="curve"]/div[6]/em[%d]/text()' % i).extract()
            #item['weatherWea']  = response.xpath('//*[@id="curve"]/div[6]/em[%d]/text()' % i).extract()
            #yield item 
        
