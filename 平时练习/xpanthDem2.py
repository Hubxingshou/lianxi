#https://xiaohua.zol.com.cn/
#https://xiaohua.zol.com.cn/detail60/59428.html
from lxml import etree
import requests
headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Mobile Safari/537.36'
    }
domain='https://xiaohua.zol.com.cn/'
def parse_page(page_url):
    resp = requests.get(page_url,headers=headers)
    text = resp.text
    #print(text)
    parse=etree.HTML(text)
    detail_url_list=parse.xpath('//ul[@class="article-list"]')

def main():
    for page in range(1,11):
        page_url="https://xiaohua.zol.com.cn/new/%s.html"%page
        parse_page(page_url)
        break
if __name__ == '__main__':
    main()