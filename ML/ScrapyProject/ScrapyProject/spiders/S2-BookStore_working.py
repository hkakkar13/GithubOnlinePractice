import scrapy
import csv

class BookStoreSpider(scrapy.Spider):
    name = "S2-BookStore2"
    no_pages = 3
    
    
        
        
    def start_requests(self):
        urls = [
            'http://books.toscrape.com/',
        ]
        
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_page)
            #yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        #yield scrapy.Request(url=url,callback=self.parse_page)
        
        next_href = response.selector.xpath('//li[@class="next"]/a/@href').get()
        
        if next_href:
            if 'catalogue' not in next_href :
                next_url = 'http://books.toscrape.com/catalogue/' + next_href
                print(f"next_url is : {next_url}")
            else :
                next_url = 'http://books.toscrape.com/' + next_href
                print(f"next_url is : {next_url}")
                
        yield scrapy.Request(next_url,callback=self.parse_page)
     
    def parse_page(self,response):
        
        with open('books.csv', mode='a',newline='') as books_csv:
            
            books_writer = csv.writer(books_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for i in range(len(response.selector.xpath('//article[@class="product_pod"]'))):
                image_url = response.selector.xpath('//article[@class="product_pod"]/div[@class="image_container"]/a/img/@src')[i].get()
                title = response.selector.xpath('//article[@class="product_pod"]/h3/a/@title')[i].get()
                price =  response.selector.xpath('//article[@class="product_pod"]/div[@class="product_price"]/p[@class="price_color"]/text()')[i].get()

                books_writer.writerow([image_url,title,price])
         
        next_href = response.selector.xpath('//li[@class="next"]/a/@href').get()
        if next_href:
            if 'catalogue' not in next_href :
                next_url = 'http://books.toscrape.com/catalogue/' + next_href
                print(f"next_url is : {next_url}")
            else :
                next_url = 'http://books.toscrape.com/' + next_href
                print(f"next_url is : {next_url}")
                
            yield scrapy.Request(next_url,callback=self.parse_page)

        

        
            

        

        
            
        

        
            