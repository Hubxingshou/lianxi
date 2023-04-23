from time import sleep

import requests
import scrapy
from lxml import etree
from mySpider.items import MyspiderItem

class DoubanSpider(scrapy.Spider):

    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/chart']

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }

    def parse(self, response):
        # 首先抓取电影列表
        movie_list = response.xpath(".//div/table/*")
        # ceshi = movie_list[0].xpath(".//a/text()").extract()
        # print((ceshi[0].replace('\n/','').split())[0])
        pl_list=[]
        urls_list = response.xpath(".//tr/td[2]/div/a/@href").extract()
        for url in urls_list:
            new_response = requests.get(url, headers=DoubanSpider.header).text
            new_parse = etree.HTML(new_response)
            #     # print(new_parse)
            pl = new_parse.xpath('.//div[3]/div[1]/div[2]/div[1]/div[3]/div/span[1]/text()')
            if pl:
                pl[0] = pl[0].replace(' ', '')
                pl[0] = pl[0].replace('\n', '')
                pl[0] = pl[0].replace('\u3000', '')
                pl_list.append(pl[0])
                print(pl[0])
            else:
                pl_list.append('---暂时爬不下来')
                print('---哥,没数据啊...该! IP暂时被封了吧  歇会儿试试')
            sleep(5)
        i=0
        for selector in movie_list:
        #   遍历每个电影列表，从其中精准抓取所需要的信息并保存为item对象
            item = MyspiderItem()
            item['id'] = i+1
            item['name'] = selector.xpath(".//td[2]/div/a/text()").extract_first().split()[0]
            item['introduce'] = selector.xpath(".//td[2]/div/p/text()").extract_first().replace('\n','')
            item['star'] = selector.xpath('.//td[2]/div/div/span[@class="rating_nums"]/text()').extract_first()
            item['comments'] = selector.xpath(".//td[2]/div/div/span[@class='pl']/text()").extract_first()
            item['describe'] = pl_list[i]
        # #     item['describe'] = selector.xpath(".//span[@class='inq']/text()").extract_first()
        # #     # print(item)
            i = i+1
            yield item  # 将结果item对象返回给Item管道
        # # 爬取网页中的下一个页面url信息
        # next_link = response.xpath("//span[@class='next']/a[1]/@href").extract_first()
        # if next_link:
        #     next_link = "https://movie.douban.com/top250" + next_link
        #     print(next_link)
        #     # 将Request请求提交给调度器
        #     yield scrapy.Request(next_link, callback=self.parse)
