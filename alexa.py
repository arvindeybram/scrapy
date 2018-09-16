from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from alexa.items import *
class alexa(BaseSpider):
    name = "alexa"
    allowed_domains = ["alexa.org"]
    start_urls = [
        "https://www.alexa.com/topsites"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/li')
	    items = []
        for site in sites:
            item = alexaSiteInfoItem()
            item['title'] = site.select('a/text()').extract()
            item['link'] = site.select('a/@href').extract()
            item['desc'] = site.select('text()').extract()
            items.append(item)
        return items
			#yield item