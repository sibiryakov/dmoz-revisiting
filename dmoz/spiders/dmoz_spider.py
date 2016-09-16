# -*- coding: utf-8 -*-
from scrapy.exceptions import DontCloseSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy import signals
from dmoz.items import DmozItem


class DmozLinkExtractor(LinkExtractor):
    def extract_links(self, response):
        links = super(DmozLinkExtractor, self).extract_links(response)
        for link in links:
            if link.url.startswith("http://www.dmoz.org/Games/"):
                yield link


class DmozSpider(CrawlSpider):
    name = 'dmoz'

    rules = (
       Rule(DmozLinkExtractor(allow_domains="www.dmoz.org"), callback='parse_item', follow=True),
    )

    start_urls = ["http://www.dmoz.org/"]

    def __init__(self, *args, **kwargs):
        super(DmozSpider, self).__init__(*args, **kwargs)
        self._follow_links = True

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(DmozSpider, cls).from_crawler(crawler, *args, **kwargs)
        spider._set_crawler(crawler)
        spider.crawler.signals.connect(spider.spider_idle, signal=signals.spider_idle)
        return spider

    def spider_idle(self):
        raise DontCloseSpider

    def parse_item(self, response):
        if response.xpath('//*[@id="sites-section"]'):
            for site_item in response.xpath("//*[@id='site-list-content']/div[@class]"):
                l = ItemLoader(item = DmozItem(), response = response)
                l.add_value('url', site_item.xpath('./div[@class="title-and-desc"]/a/@href').extract_first())
                l.add_value('title', site_item.xpath('./div[@class="title-and-desc"]/a/div/text()').extract())
                l.add_value('descr', site_item.xpath('./div[@class="title-and-desc"]/div[@class="site-descr "]/text()').extract())
                yield l.load_item()

    parse_start_url = parse_item
