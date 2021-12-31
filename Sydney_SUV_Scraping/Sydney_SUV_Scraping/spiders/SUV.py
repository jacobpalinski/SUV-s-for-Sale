import scrapy


class SuvSpider(scrapy.Spider):
    name = 'SUV'
    allowed_domains = ['carsales.com.au']
    

    def start_requests(self):
        yield scrapy.Request(url='https://www.carsales.com.au/cars/new-south-wales-state/sydney-region/suv-bodystyle/?offset=0',callback=self.parse,
        headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})

    def parse(self, response):

        SUV_body= response.xpath("//div[@class='card-body']")

        for SUV in SUV_body:
            yield{
            'Title':SUV.xpath(".//h3/a/text()").get(),
            'Price':SUV.xpath(".//div[@class='price']/a/text()").get(),
            'Odometer':SUV.xpath(".//ul[@class='key-details']/li[@data-type='Odometer']/text()").get(),
            'Transmission':SUV.xpath(".//ul[@class='key-details']/li[@data-type='Transmission']/text()").get(),
            'Engine':SUV.xpath(".//ul[@class='key-details']/li[@data-type='Engine']/text()").get()
            }
        
        next_page=response.xpath("//a[@class='page-link next ']/@href").get()
        next_page_https='https://www.carsales.com.au'+ next_page

        if next_page:
           yield scrapy.Request(url=next_page_https,callback=self.parse,headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})
    

