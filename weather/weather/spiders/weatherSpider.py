import scrapy
from ..items import WeatherItem 
 
class CatchWeatherSpider(scrapy.Spider):
    name = 'CatchWeather'
    allowed_domains = ['weather.com.cn']
    start_urls = [
        "http://www.weather.com.cn/weather/101280101.shtml"
    ]
     
    def parse(self, response):
        for sel in response.xpath('//*[@id="7d"]/ul/li'):
            item = WeatherItem()
            item['weatherDate'] = sel.xpath('h1/text()').extract() 
            #item['weatherWea'] = sel.xpath('p[@class="wea"]/text()').extract()
            #print(response.xpath('//*[@id="around"]/div[1]/ul/li[1]/a/span/text()').extract())
            #print(response.xpath('//*[@id="curve"]/div[1]/em[1]/text()').extract())
            item['weatherWea'] = sel.xpath('p[1]/text()').extract()
            item['weatherTem1'] = sel.xpath('p[@class="tem"]/span/text()').extract()
            item['weatherTem2'] = sel.xpath('p[@class="tem"]/i/text()').extract()
            item['weatherWin'] = sel.xpath('p[@class="win"]/i/text()').extract()
            yield item

