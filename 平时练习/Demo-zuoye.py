from urllib import request

url = 'http://www.biedoul.com/'
res = request.urlopen(url)
print(res.read().decode('utf-8'))

# for i in range(100,110):
#     url = 'http://www.biedoul.com/index/'+str(i)  #转为字符串进行拼接
#     res = request.urlopen(url)
#     print(res.read().decode('utf-8'))

# 网页进入不了