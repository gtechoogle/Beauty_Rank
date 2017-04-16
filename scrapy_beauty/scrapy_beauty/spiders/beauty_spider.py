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
            # yield {
            #     'title': post.xpath("@title").extract_first(),
            #     'link': post.xpath("@href").extract_first(),
            # }
            details_link = response.xpath('//ul[@id="post_container"]//div[@class="thumbnail"]//a/@href').extract_first();
            print post.xpath("@title").extract_first()
            print details_link
            if details_link is not None:
                print "#######"
                yield scrapy.Request(details_link, callback=self.parse_image)
    
    # def parse(self, response):
    #     for post in response.xpath('//ul[@id="post_container"]//div[@class="thumbnail"]//a') :
    #         yield {
    #             #'link': post.xpath("@href").extract_first(),
    #             #'title': post.xpath("@title").extract_first()
    #         }
    #     details_link = response.xpath('//ul[@id="post_container"]//div[@class="thumbnail"]//a/@href').extract_first();
    #     if details_link is not None:
    #         yield scrapy.Request(details_link, callback=self.parse_image)
    #     next_page = response.xpath('//div[@class="pagination"]/a[@class="next"]/@href').extract_first()
    #     if next_page is not None:
    #         yield scrapy.Request(next_page, callback=self.parse)
    
    def parse_image(self, response):
        print "parse_image"
        for img_link in response.xpath('//div[@id="post_content"]//img'):
            yield {
                'image_link': img_link.xpath("@src").extract_first()
            }
        next_image = response.xpath('//li[@class="page-next"]//a/@href').extract_first()
        if next_image is not None:
            yield scrapy.Request(next_image, callback=self.parse_image);

