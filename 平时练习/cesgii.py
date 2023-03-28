import urllib
from lxml import etree
import jsonpath
import requests
from urllib import parse
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }
joke_list=[]
domain = "https://careers.tencent.com/"
detail_url_list = parse.xpath(
        '//div[@class="job-list"]//a[@class="job-list-link"]/@href')
#print(detail_url_list) #list ：点击“查看全文”源代码中a标签中href的值
for detail_url in detail_url_list:
    detail_url = domain + detail_url
    print(detail_url) # 点击查看全文后的url

resp = requests.get(detail_url,headers=headers)
text = resp.text
parse=etree.HTML(text)
joke_title=parse.xpath('//h4[@class="recruit-title"]/text()')[0]
joke_content="".join(parse.xpath('//a[@class="recruit-tips"]//text()')).strip()
joke_list.append(
        {
            'title':joke_title,
            'content':joke_content
         })
print(joke_list)