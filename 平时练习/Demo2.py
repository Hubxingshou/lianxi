import urllib.request  #请求模块
import urllib.parse     # url解析模块

 #类似模拟post请求     urlencode :字节流转换
url = 'http://httpbin.org/post'
data = bytes(urllib.parse.urlencode({'world':'hello'}).encode('utf-8'))
#print(data)
response = urllib.request.urlopen(url,data=data)
print(response.read())