# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # ranking = scrapy.Field()  # 排名
    id = scrapy.Field()  # 方便调试,顺序
    name = scrapy.Field()  # 电影名
    introduce = scrapy.Field()  # 演员表
    star = scrapy.Field()  # 评分
    comments = scrapy.Field()  # 评论数
    describe = scrapy.Field()  # 故事简介



