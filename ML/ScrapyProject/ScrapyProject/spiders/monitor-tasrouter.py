import scrapy

class TasrouterSpider(scrapy.Spider):
    name = "monitor-tasrouter"
    
    def start_requests(self):
        urls =[
        'https://10.52.201.155:7630/cib/live',
        ]
        
        for url in urls:
            yield scrapy.http.Request(url=url,callback=self.parse)
            
    def parse(self,response):
        filename = "tasrouter.txt"
        with open("tasrouter.txt",mode="wb") as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
    
    