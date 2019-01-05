# -*- coding: utf-8 -*-
import scrapy
import sys,os,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        print(response.text)
