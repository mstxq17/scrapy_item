# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #序号
    id_ = scrapy.Field()
    # 百度搜索域名
    domain = scrapy.Field()
    # 搜索标题
    title = scrapy.Field()

