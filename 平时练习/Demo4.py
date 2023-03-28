import urllib.parse
url = 'https://www.baidu.com/index.html;user?id=S#comment'
result = urllib.parse.urlparse(url)
print(result)
print(result.scheme)
print(result.netloc)
print(result.path)
print(result.params)