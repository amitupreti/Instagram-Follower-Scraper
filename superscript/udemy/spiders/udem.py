# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
import scrapy_proxies




class UdemySpider(scrapy.Spider):
    name = 'udem'
    rotate_user_agent = True

    allowed_domains = ['google.com']
    start_urls = [r"https://www.google.com/maps/place/Pike's+Landing/@64.8299557,-147.8510661,17z/data=!4m5!3m4!1s0x0:0xd609c9524d75cbc7!8m2!3d64.8299557!4d-147.8488774?hl=us"]

    def parse(self, response):
        yield SplashRequest(response.url, callback=self.parse1, dont_filter=True)


    def parse1(self, response):
        address = response.xpath('//*[@data-section-id="ad"]//text()').extract()
        plus_code =response.xpath('//*[@data-section-id="ol"]//text()').extract()
        website =response.xpath('//*[@data-section-id="ap"]//text()').extract()
        phone =response.xpath('//*[@data-section-id="pn0"]//text()').extract()
        open_hours =  response.xpath('//*[@class="section-info section-open-hours"]//text()').extract()
        mrnu =  response.xpath('//*[@data-section-id="m"]//text()').extract()
        no_of_reviews = response.xpath('//*[@class="section-star-display"]//text()').extract()
        rating  = response.xpath('//*[@jsaction="pane.rating.moreReviews"]//text()').extract()
        desc = response.xpath('//*[@class="section-editorial section-editorial-button ripple-container"]//text()').extract()
        category = response.xpath('//*[@jsaction="pane.rating.category"]//text()').extract()
        image = response.xpath('//*[@jsaction="pane.heroHeader.heroImage"]/img/@src').extract()
       
        print(address,plus_code,website,phone,open_hours,rating,no_of_reviews)