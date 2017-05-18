# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	# define the fields for your item here like:
    # name = scrapy.Field()
    city_code = scrapy.Field()
    weatherDate = scrapy.Field()
    weatherWea = scrapy.Field()
    weatherTem1 = scrapy.Field()
    weatherTem2 = scrapy.Field()
    weatherWin = scrapy.Field()
