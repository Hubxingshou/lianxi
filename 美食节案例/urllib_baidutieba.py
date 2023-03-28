import urllib
import urllib.request
import urllib.parse
import requests

def load_page(url,file_name):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    request=urllib.request.Request(url,headers=headers)
    return urllib.request.urlopen(request).read()

def write_page(html,file_name):
    with open(file_name,'w',encoding='utf-8') as file:
        file.write(html.decode('utf-8'))

def tieba_spider(url, begin_page, end_page):
    for page in range(begin_page, end_page + 1):
        pn = (page - 1) * 50
        file_name = '第' + str(page) + "页.html"
        full_url = url + "&pn=" + str(pn)
        html = load_page(full_url, file_name)
        write_page(html, file_name)

if __name__ == '__main__':
    kw=input("请输入需要爬取的贴吧名称：")
    begin_page=int(input("请输入起始页："))
    end_page = int(input("请输入结束页："))
    url='https://tieba.baidu.com/f?'
    key=urllib.parse.urlencode({'kw':kw})
    url=url+key
    tieba_spider(url,begin_page,end_page)





