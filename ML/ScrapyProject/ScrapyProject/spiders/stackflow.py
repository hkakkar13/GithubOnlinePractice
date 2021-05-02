import scrapy

class Stackflow(scrapy.Spider):
    name = "stackflow"
    
    def start_requests(self):
        urls = [
            'https://stackoverflow.com/questions?pagesize=50&sort=newest',
        ]
        
        for url in urls:
            yield scrapy.Request(url,callback=self.parse)
        
    def parse(self,response):
        sel = scrapy.Selector(response)
        questions = sel.xpath('//div[@class="summary"]/h3')
        
        for question in questions:
            print(question)
    