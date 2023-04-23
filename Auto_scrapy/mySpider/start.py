# -*- coding:utf-8 -*-
# data = 2023/4/18 22:09
# Author: lyi Head  working
# project_name : Pythonpachong
from scrapy import cmdline
cmdline.execute(("scrapy crawl douban -o data.json ".split()))