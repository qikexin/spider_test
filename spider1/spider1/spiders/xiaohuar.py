# -*- coding: utf-8 -*-
import scrapy
# import sys,os,io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
from scrapy.selector import HtmlXPathSelector,Selector
from scrapy.http.request import Request
from scrapy.http.cookies import CookieJar
class XiaohuarSpider(scrapy.Spider):
    name = 'xiaohuar'
    allowed_domains = ['http://www.xiaohuar.com/']
    start_urls = ['http://www.xiaohuar.com//']

    def parse(self, response):
        hxs = Selector(response=response)
        hxa = HtmlXPathSelector(response)

        print(response.url)
        result = hxs.xpath('//img')
        print(result)

        # 放到调度器中使用下面固定的规则
        # for url in result:
        #     cookie_jar = CookieJar()
        #     cookie_jar.extract_cookies(response,response.request)
        #     yield Request(url=url,callable=self.parse)