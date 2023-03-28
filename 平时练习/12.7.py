import re
import requests
def parse_page(parurl_page):
    headers = {
        'User_Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Mobile Safari/537.36'
    }
    resp = requests.get(parurl_page,headers=headers)
    text = resp.text
    contents = re.findall(r'<div\sclass="content">.*?<span>(.*?)</span>',text,re.DOTALL)
    duanzi=[]
    for content in contents:
        x=re.sub(r'<.*?>','',content)
        duanzi.append(x.strip())
        print(x.strip())
        print('='*100)
def main():
    #https://www.qiushibaike.com/text/page/1/
    for i in range(1,11):
        pars_url='https://www.qiushibaike.com/text/page/%s/'%i
        parse_page(pars_url)
        
if __name__ == '__main__':
    main()