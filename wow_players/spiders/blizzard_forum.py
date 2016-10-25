# -*- coding: utf-8 -*-
import scrapy


class BlizzardForumSpider(scrapy.Spider):
    name = "blizzard_forum"
    allowed_domains = ["us.battle.net"]
    start_urls = ['http://us.battle.net/forums/pt/wow/']

    def parse(self, response):
        """Create request to first page"""
        forum_cards = response.css('.ForumCards a').xpath('@href').extract()

        for card in forum_cards:
            url = "http://us.battle.net{}".format(card)
            request = scrapy.Request(
                url=url,
                callback=self.parse_forum_topic,
            )
            yield request

    def parse_forum_topic(self, response):
        import ipdb
        ipdb.set_trace()
