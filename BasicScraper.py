import scrapy,os,sys
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class FollowAllSpider(CrawlSpider):
	name = 'follow_all'
	start_urls = ['https://www.youtube.com/watch?v=tk36ovCMsU8&index=12&list=PLcYK4PlHbZQvbWClI38SfOjBt3godBsY1']
	rules = [Rule(LinkExtractor(), callback='parse_item', follow=True)]
	
	def parse_item(self, response):
	
		MAX_RANGE = 1000
		count=0 
		f = open("test.csv",'w+') 
		for href in response.css('a::attr(href)'):
			count+=1
			if count <= MAX_RANGE:
				f.write((str(href)+'\n').replace('<Selector xpath=\'descendant-or-self::a/@href\' data=\'','').replace('\'>',''))
			else:
				break
		f.close()
			
				
			