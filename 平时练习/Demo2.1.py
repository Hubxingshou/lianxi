import urllib
from urllib import  request
from urllib import  parse

url = "http://www.baidu.com/s"
#https://www.baidu.com/s?wd=%E6%89%AC%E5%B7%9E
#https://www.baidu.com/s?wd=%E6%89%AC%E5%B7%9E
word = {"wd":"扬州"}
word = parse.urlencode(word)
#print(word)
new_url = url+'?'+word

headers={
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Mobile Safari/537.36'
}

req=request.Request(new_url,headers=headers)
response=request.urlopen(req)
html = response.read().decode('utf-8')
print(html)
# import urllib.request
# url = "http://ypi.jiastudy.cn/"
# response = urllib.request.urlopen(url)
# print(type(response))
# html = response.read().decode('utf-8')
# #print(html)
# url1='https://www.baidu.com'
#urllib.request.urlretrieve(url,'baidu.html')