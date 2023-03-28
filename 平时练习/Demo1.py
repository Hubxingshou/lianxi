import urllib.request
url='https://www.csdn.net/'

response = urllib.request.urlopen(url)

html = response.read().decode('utf-8')
print(html)
url='https://y.qq.com/n/ryqq/player'

# urllib.request.urlretrieve(url,'qqyy.html')