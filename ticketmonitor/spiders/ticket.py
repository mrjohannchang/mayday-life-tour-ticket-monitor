# -*- coding: utf-8 -*-
import scrapy


class TicketSpider(scrapy.Spider):
    name = 'ticket'
    allowed_domains = ['www.bin-music.com']
    start_urls = ['http://www.bin-music.com/events/mayday/2017MaydayLiFE/']

    def parse(self, response):
        for row in response.css('ul.sold'):
            for column in row.css('li'):
                if column.css('div.datewrap').css('div.city').css('p::text').extract() != ['Anaheim']:
                    continue
                if column.css('div.status').re(r'COMING\ SOON'):
                    continue
                yield {}
