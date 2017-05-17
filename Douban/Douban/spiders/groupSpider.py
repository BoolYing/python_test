# coding=utf-8
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from ..items import DoubanItem
class GroupSpider(CrawlSpider):
    name = "Douban"
    allowed_domains = ["douban.com"]
    start_urls = ["http://www.douban.com/group/explore?tag=%E7%A4%BE%E7%A7%91"]

    rules = [
        Rule(SgmlLinkExtractor(allow=(r'/group/explore\?start=.*', )), callback='parse_next_page'),
    ]

    def parse_next_page(self, response):
        item = DoubanItem()
        sel = response.xpath("//div[@class='group-list']/div[@class='result']")
        for s in sel:
            info = s.xpath("div/div/h3/a/text()").extract()
            item["groupName"] = info
            yield item
