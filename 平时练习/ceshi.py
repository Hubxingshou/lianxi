#coding=gbk
import urllib.request  #请求模块
import ssl
#import urllib.parse     # url解析模块
# url = 'http://httpbin.org'
# #SSl错误时：
# context = ssl._create_unverified_context()
# re = urllib.request.urlopen(url,context=context)
# print(re.geturl())   # 网址
# print(re.getcode())  # 状态码
# print(re.info())     # 返回页面信息
#
#
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"*",j,"=",i*j,end=" ")
#     print()

for i in range(9,0,-1):
    for j in range(1,i+1):
        print(i, "*", j, "=", i * j, end=" ")
    print()

for i in range(1,10):
    for j in range(1,10-i):
        print(end='       ')   #每个算法长度6，加上1个空位符，最少7个占位符
        for k in  range(1,i+1):
            print("%d*%d=%2d"%(k,i,k*i),end=' ')
            print("")#方式二：通过【while】方式实现i=1while i<10:    k=1    while k<10-i:        print(end='       ')        k+=1    j = 1    while j<=i:        print("%d*%d=%2d"%(j,i,j*i),end=' ')        j+=1    print("")    i+=1 输出：3. 左上三角形#方式一：通过【for..in..】方法实现for i in range(9,0,-1): #参数：计数从9开始，0结束，步长-1    for j in range(1,i+1):         print("%d*%d=%2d"%(j,i,j*i),end=' ')    print("")#方式二：通过【while】方法实现i=9while i>=1:    j = 1    while j<=i:        print("%d*%d=%2d"%(j,i,j*i),end=' ')        j+=1    print("")    i-=1输出：4. 右上三角形#方式一：通过【for..in..】方法实现for i in range(9,0,-1):    for j in range(1,i+1):         print("%d*%d=%2d"%(j,i,j*i),end=' ')    print("")    for k in range(i,10):         print(end='       ')#方式二：通过【while】方法实现i=9while i>=1:    k=9    while k>i:        print(end='       ')        k-=1    j = 1    while j<=i:        print("%d*%d=%2d"%(j,i,j*i),end=' ')        j+=1    print("")    i-=1输出：