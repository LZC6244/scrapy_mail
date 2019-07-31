# -*- coding: utf-8 -*-
import scrapy
from maida.mail import EmailSender


class TestSpider(scrapy.Spider):
    name = 'test'
    # allowed_domains = []
    start_urls = [
        'http://www.baidu.com/',
        'https://github.com/LZC6244',
        'https://www.runoob.com/',
        'https://cn.bing.com/',
        'http://tool.oschina.net/uploads/apidocs/jquery/regexp.html'
    ]

    def parse(self, response):
        a = response.xpath('asd').extract()[0]
