from urllib import  request
from urllib import  parse
# https://fanyi.youdao.com/
url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Mobile Safari/537.36'
}
formdata = {
    'i': '篮球',
    'from':' AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '16383582626343',
    'sign': '053425e866a6f51ecfa86842fce30b28',
    'lts':'1638358262634',
    'bv': '84f204676437161700241e810380a355',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
}
data = bytes(parse.urlencode(formdata).encode('utf-8'))
req=request.Request(url,data=data,headers=headers)
response=request.urlopen(req)
html = response.read().decode('utf-8')
print(html)