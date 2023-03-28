import requests
import time
from bs4 import BeautifulSoup
# https://movie.douban.com/top250
# https://movie.douban.com/
# https://movie.douban.com/top250?start=50&filter=
headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}
def get_detail_url(url):
    resp = requests.get(url,headers=headers)
    html = resp.text
    soup = BeautifulSoup(html,'lxml')
    li_list = soup.find('ol',class_='grid_view').find_all('li')
    detail_urls=[]
    for li in li_list:
        detail_url = li.find('a')['href']
        detail_urls.append(detail_url)
    return detail_urls
def parse_detail(detaile_urls,f):
    for detaile_url in detaile_urls:
        resp = requests.get(detaile_url, headers=headers)
        html = resp.text
        soup = BeautifulSoup(html, 'lxml')
        name = list(soup.find('div',id='dale_movie_subject_top_icon').find('h1'))
        name = ''.join(name)
        print(name)


def main():
    for page in range(0,101,25):
        url = f'https://movie.douban.com/top250?start={page}&filter='
        #print(url)
        detail_urls=get_detail_url(url)

        with open('douban.csv','a',encoding='utf-8') as f:
            parse_detail(detail_urls,f)
        time.sleep(2)


if __name__ == '__main__':
    main()