import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector

class MySpider(CrawlSpider):
	name = 'alexa'
	allowed_domains = ['wikipedia.org']
	start_urls = ['https://en.wikipedia.org/wiki/Yahoo!_Directory']
	
	rules=(
		Rule(LinkExtractor(allow=('wiki/global;\d', ), restrict_xpaths=('//a[@class="next"]', )), callback='parse_item',follow= True),
	)
	
	def start_requests(self):
		return self.parse(response)

	def parse_item(self, response):
		item = AlexaItem()
		item['name']=response.xpath('//div[@class="desc-container"]/p[@class="desc-paragraph"]/a/text()').extract()
		return item