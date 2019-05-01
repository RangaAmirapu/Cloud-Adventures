import scrapy
from scrapy.loader import ItemLoader
from dailyquotes.items import DailyquotesItem

class GoodReadSpider(scrapy.Spider):
    #identity
    name = 'goodreads'

    #requests
    def start_requests(self):
        url = 'https://www.goodreads.com/quotes?page=1'
        
        yield scrapy.Request(url=url, callback=self.parse)

    #response
    def parse(self, response):
        for quote in response.selector.xpath('//div[@class="quote"]'):

            loader = ItemLoader(item=DailyquotesItem(), selector=quote, response=response)
            loader.add_xpath('text', './/div[@class="quoteText"]/text()[1]')
            loader.add_xpath('author', './/span[@class="authorOrTitle"]/text()')
            loader.add_xpath('tags', './/div[@class="greyText smallText left"]/a')

            yield loader.load_item()
             
        next_page = response.selector.xpath('//a[@class="next_page"]/@href').extract_first()

        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url = next_page_link, callback=self.parse)
    