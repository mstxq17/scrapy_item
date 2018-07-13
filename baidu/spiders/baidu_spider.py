# -*- coding: utf-8 -*-
import scrapy
from baidu.items import BaiduItem

class BaiduSpiderSpider(scrapy.Spider):
    name = 'baidu_spider'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/s?wd=site:usc.edu.cn']

    def parse(self, response):
        # print(response.text)
        url_list = response.xpath('//div[@id="content_left"]/div')
        #print url_list
        for i_item in url_list:
        	baidu_item = BaiduItem()
        	baidu_item['id_']=i_item.xpath('./@id').extract_first()
        	domain=i_item.xpath('.//div[@class="f13"]/a[1]/text()').extract_first()
        	if domain:
        		baidu_item['domain']=domain.split('/')[0]
        	else:
        		baidu_item['domain']=None
        	baidu_item['title']=i_item.xpath('.//h3[@class="t"]/a[1]/text()').extract_first()
        	# print baidu_item
        	yield baidu_item
        next_link = response.xpath('//*[@id="page"]/a[last()][@class="n"]/@href').extract()
        if next_link:
        	next_link = next_link[0]
        	yield scrapy.Request("http://www.baidu.com"+next_link,callback=self.parse)





        


