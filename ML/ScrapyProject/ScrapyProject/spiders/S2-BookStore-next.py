import scrapy
import csv

class BookStoreSpider(scrapy.Spider):
    name = "S2-BookStore-next"
    no_pages = 1
    
    
        
        
    def start_requests(self):
        urls = [
            'http://books.toscrape.com/',
        ]
        
        for url in urls:
            #yield scrapy.Request(url, callback=self.parse)
            self.parse_first_page()
            yield scrapy.Request(url, callback=self.parse_next_page)
            #yield scrapy.Request(url, callback=self.parse)
            
    def parse_first_page(self):
        
        with open('books.csv', mode='w',newline='') as csv_file:
            fieldnames = ['image_url','book_title','product_price']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
   
    def parse_next_page(self,response):
        
        #self.no_pages = self.no_pages - 1
        print(f"the value of no_pages is {self.no_pages}")
        
        if self.no_pages <= 50 :

            with open('books.csv', mode='a',newline='') as books_csv:

                books_writer = csv.writer(books_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                for i in range(len(response.selector.xpath('//article[@class="product_pod"]'))):
                    image_url = response.selector.xpath('//article[@class="product_pod"]/div[@class="image_container"]/a/img/@src')[i].get()
                    title = response.selector.xpath('//article[@class="product_pod"]/h3/a/@title')[i].get()
                    price =  response.selector.xpath('//article[@class="product_pod"]/div[@class="product_price"]/p[@class="price_color"]/text()')[i].get()

                    books_writer.writerow([image_url,title,price])
            
            self.no_pages = self.no_pages + 1
            next_href = response.selector.xpath('//li[@class="next"]/a/@href').get()
            
            if next_href:
                if 'catalogue' not in next_href :
                    next_url = 'http://books.toscrape.com/catalogue/' + next_href
                    print(f"next_url is : {next_url}")
                else :
                    next_url = 'http://books.toscrape.com/' + next_href
                    print(f"next_url is : {next_url}")
                    
                
                 

                yield scrapy.Request(next_url,callback=self.parse_next_page)

        

        
            

        

        
            
        

        
            