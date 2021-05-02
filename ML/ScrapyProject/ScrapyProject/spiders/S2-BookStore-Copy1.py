import scrapy
import csv

class BookStoreSpider(scrapy.Spider):
    name = "S2-BookStore1"
    
    def start_requests(self):
        #base_url = 'http://books.toscrape.com/catalogue/'
        #i = 1
        '''
        for i in range(3):
            
            url = base_url + href_value
        
        '''
        urls = [
            'http://books.toscrape.com/',
        ]
        
              
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        
        #no_books = response.selector.xpath('//article[@class="product_pod"]')
        
        with open('books.csv', mode='a',newline='') as books_csv:
            books_writer = csv.writer(books_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            for i in range(len(response.selector.xpath('//article[@class="product_pod"]'))):
                image_url = response.selector.xpath('//article[@class="product_pod"]/div[@class="image_container"]/a/img/@src')[i].get()
                title = response.selector.xpath('//article[@class="product_pod"]/h3/a/@title')[i].get()
                price = response.selector.xpath('//article[@class="product_pod"]/div[@class="product_price"]/p[@class="price_color"]/text()')[i].get()

                
                books_writer.writerow([image_url,title,price])
            
        
        
        
        