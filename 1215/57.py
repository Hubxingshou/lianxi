import urllib.request
import urllib.parse
url = "http://www.baidu.com/s"
word={"wd":"传智播客"}
word=urllib.parse.urlencode(word)
# print(word)
new_url = url + "?" +word
# print(new_url)
headers = {
        'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Mobile Safari/537.36",
}
chuandi = urllib.request.Request(new_url,headers=headers)
# print(chuandi)
reponse=urllib.request.urlopen(chuandi)
html=reponse.read().decode('utf-8')
print(html)