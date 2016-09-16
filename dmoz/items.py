# -*- coding: utf-8 -*-
import scrapy


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    descr = scrapy.Field()
    url = scrapy.Field()
