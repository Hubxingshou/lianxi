import urllib.parse


data={"name":"Alice","age":18,"address":"CHN"}
qs=urllib.parse.urlencode(data)
print(qs)
print(urllib.parse.parse_qs(qs))
print(urllib.parse.unquote(qs))