from urllib import request
from urllib import parse

url = 'http://www.itcast.cn'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Mobile Safari/537.36'
}
data = bytes(parse.urlencode({'name':'itcast'}).encode('utf-8'))
rq = request.Request(url,data=data,headers=headers)

resp = request.urlopen(rq)

html=resp.read().decode('utf-8')
print(html)