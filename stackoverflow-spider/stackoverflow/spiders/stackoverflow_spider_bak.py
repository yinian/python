#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

import scrapy
from stackoverflow.spiders.items import StackoverflowItem

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('monitor')
logger.setLevel(logging.INFO)

fh = logging.FileHandler('monitor.log')
fh.setLevel(logging.INFO)

fh.setFormatter(formatter)
logger.addHandler(fh)


class StackoverflowSpider(scrapy.Spider):

    name = "stackoverflow"

    def __init__(self):
        self.count = 1

    def start_requests(self):
        _url = 'https://stackoverflow.com/questions?sort=votes&page={page}&pagesize=50'
        urls = [_url.format(page=page) for page in range(1, 100001)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for index in range(1, 51):
            self.count += 1
            if self.count % 100 == 0:
                logger.info(self.count)

            sel = response.xpath(
                '//*[@id="questions"]/div[{index}]'.format(index=index))
            item = StackoverflowItem()
            item['votes'] = sel.xpath(
                'div[@class="statscontainer"]/div[@class="stats"]/div[@class="vote"]/div[1]/span/strong/text()'
            ).extract()
            # print(item['votes'])
            item['answers'] = sel.xpath(
                'div[@class="statscontainer"]/div[@class="stats"]/div[2]/strong/text()'
            ).extract()
            item['views'] = "".join(
                sel.xpath('div[@class="statscontainer"]/div[2]/@title').
                extract()).split()[0].replace(",", "")
            item['questions'] = sel.xpath(
                'div[@class="summary"]/h3/a/text()').extract()
            item['links'] = "https://stackoverflow.com".join(sel.xpath('div[@class="summary"]/h3/a/@href').extract())
            item['tags'] = sel.xpath(
                'div[@class="summary"]/div[2]/a/text()').extract()
            yield item