# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubtSpiderSpider(scrapy.Spider):
    # 爬虫名字
    name = 'doubt_spider'
    allowed_domains = ['movie.douban.com']
    #入口url spider->引擎->调度器
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        # print(response.text)
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i_item in movie_list:
        	douban_item = DoubanItem()
        	douban_item['serial_number'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first()
        	douban_item['movie_name']= i_item.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
        	content = i_item.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
        	for i_content in content:
        		content_s = "".join(i_content.split())
        		douban_item['introduce']=content_s
        	yield douban_item
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
        	next_link = next_link[0]
        	yield scrapy.Request("https://movie.douban.com/top250"+next_link,callback=self.parse)
        	# douban_item['start']=
        	# douban_item['evaluate']=
        	# douban_item['describe']=