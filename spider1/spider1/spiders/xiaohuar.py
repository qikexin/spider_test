# -*- coding: utf-8 -*-
import scrapy
import  import sys,os,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
from scrapy.selector import HtmlXPathSelector
class XiaohuarSpider(scrapy.Spider):
    name = 'xiaohuar'
    allowed_domains = ['http://www.xiaohuar.com/']
    start_urls = ['http://http://www.xiaohuar.com//']

    def parse(self, response):
        print(response.text)
