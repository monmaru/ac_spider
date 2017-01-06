# -*- coding: utf-8 -*-
import scrapy

from ac_spider.items import AcSpiderItem


class AcSpider(scrapy.Spider):
    name = 'ac_spider'
    allowed_domains = ['qiita.com']

    start_urls = (
        'http://qiita.com/advent-calendar/2016/categories/programming_languages',
        'http://qiita.com/advent-calendar/2016/categories/libraries',
        'http://qiita.com/advent-calendar/2016/categories/databases',
        'http://qiita.com/advent-calendar/2016/categories/web_technologies',
        'http://qiita.com/advent-calendar/2016/categories/mobile',
        'http://qiita.com/advent-calendar/2016/categories/devops',
        'http://qiita.com/advent-calendar/2016/categories/services',
    )

    def parse(self, response):
        for href in response.css('.adventCalendarList .adventCalendarList_calendarTitle > a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_item)

    def parse_item(self, response):
        yield {
            'category': response.css('h1::text').extract(),
            'articles': [self.extract_article(entry) for entry in response.css('.adventCalendarItem_entry')],
        }

    @staticmethod
    def extract_article(entry):
        article = AcSpiderItem()
        article['title'] = entry.css('a::text').extract()
        article['url'] = entry.css('a::attr(href)').extract()
        return article
