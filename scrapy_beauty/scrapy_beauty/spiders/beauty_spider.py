import scrapy

class BeautySpider(scrapy.Spider):
    name = 'beauty'
    def start_requests(self, parameter_list):
        urls = [
            'http://www.nanrencd.cc/'
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self, response):
         page = response.url.split("/")[-2]