import scrapy

class BeautySpider(scrapy.Spider):
    name = 'beauty'
    def start_requests(self):
        urls = [
            'http://www.nanrencd.cc/'
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self, response):
        for post in response.xpath('//ul[@id="post_container"]//div[@class="thumbnail"]//a') :
            yield {
                'link': post.xpath("@href").extract_first(),
                'title': post.xpath("@title").extract_first(),
            }