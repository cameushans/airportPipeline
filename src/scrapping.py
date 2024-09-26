import scrapy
from scrapy.crawler import CrawlerProcess
import pandas 

class UfcSpider(scrapy.Spider):
    
    data = dict()
    name: str = 'ufcspider'
    start_urls: list[str]= ['http://www.ufcstats.com/statistics/fighters?char=a&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=b&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=c&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=d&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=e&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=f&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=g&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=h&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=i&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=j&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=k&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=l&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=m&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=n&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=o&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=p&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=q&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=r&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=s&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=t&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=u&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=v&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=w&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=x&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=y&page=all',
                            'http://www.ufcstats.com/statistics/fighters?char=z&page=all'
                            ]

    def parse(self, response) -> None:
        res = response.xpath('//a[@class="b-link b-link_style_black"]/text()'
                      ).getall()
        
        data = [{'name': value} for value in res]
        
        
        df = pandas.DataFrame(data)
        df.to_csv('./ufc.csv',  mode='w', index=True)
        print(df)
            
process = CrawlerProcess()
process.crawl(UfcSpider)
process.start()
