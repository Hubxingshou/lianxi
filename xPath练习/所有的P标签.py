from lxml import etree
import json
import requests
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
wangye='http://category.dangdang.com/cp01.49.05.11.00.00.html'

resp = requests.get(wangye,headers=headers)
text = resp.text
# print(text)
parse=etree.HTML(text)[0]
detail_url_list=parse.xpath('/html/body/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/p[5]/span[1]/a[1]/text()')
print(detail_url_list)
# with open("数据分析实例.txt", 'w', encoding='utf-8') as fp:
#     json.dump(detail_url_list, fp, ensure_ascii=False)

