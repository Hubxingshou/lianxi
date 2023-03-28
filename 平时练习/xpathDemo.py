#https://xiaohua.zol.com.cn/
#https://xiaohua.zol.com.cn/detail60/59428.html
# 网站首页：
# # https://xiaohua.zol.com.cn
# 点击最新笑话后的页面：每一页的url：
# # https://xiaohua.zol.com.cn/new/4.html
# 点击笑话中的查看全文按钮后进入的页面：
# # https://xiaohua.zol.com.cn/detail60/59031.html
# 点击查看全文后检查 代码，发现url后面部分的字符串：
# # /detail60/59031.html
import jsonpath
import json
from lxml import etree
import requests
headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Mobile Safari/537.36'
    }
domain='https://xiaohua.zol.com.cn/'
joke_list=[]

def parse_page(page_url):
    resp = requests.get(page_url,headers=headers)
    text = resp.text
    #print(text)
    parse=etree.HTML(text)
    detail_url_list=parse.xpath('//ul[@class="article-list"]//li[@class="article-summary"]//a[@class="all-read"]/@href')
    #print(detail_url_list) #list ：点击“查看全文”源代码中a标签中href的值
    for detail_url in detail_url_list:
        detail_url = domain+detail_url
        #print(detail_url) # 点击查看全文后的url
        parse_detail(detail_url)  #继续抓取笑话的详细内容
        #break
def parse_detail(detail_url):
    resp = requests.get(detail_url,headers=headers)
    text = resp.text
    parse=etree.HTML(text)
    joke_title=parse.xpath('//h1[@class="article-title"]/text()')[0]
    # parse.xpath('//h1[@class="article-title"]/text()')的返回值是一个列表，列表中只有一个元素（标题）
    # list[0]:访问列表中第一个元素
    joke_content="".join(parse.xpath('//div[@class="article-text"]//text()')).strip()
    # parse.xpath('//div[@class="article-text"]//text()')：返回值是一个列表，多个元素，一个列表一个笑话内容
    # "".join()：此方法可以将列表元素拼接在一起
    # strip():去掉空白字符
    # print(joke_title)
    # print(joke_content)
    # print("="*100)
    joke_list.append(
        {
            'title':joke_title,
            'content':joke_content
         })
    # print(joke_list)

def main():
    for page in range(1,11):
        page_url=f"https://xiaohua.zol.com.cn/new/{page}.html"
        parse_page(page_url)
        

    with open("xiaohua1.txt",'w',encoding='utf-8') as fp:
        json.dump(joke_list,fp,ensure_ascii=False)

if __name__ == '__main__':
    main()