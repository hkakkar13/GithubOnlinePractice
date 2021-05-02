import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes-Spider"
    
    def start_requests(self):
        urls =[
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]
        for url in urls:
            yield scrapy.http.Request(url=url,callback=self.parse)
    
    def parse(self,response):
        page = response.url.split('/')[-2]
        filename = f'quotes-{page}.html'
        
        with open(filename,mode="wb") as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')