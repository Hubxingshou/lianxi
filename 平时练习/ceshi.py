#coding=gbk
import urllib.request  #����ģ��
import ssl
#import urllib.parse     # url����ģ��
# url = 'http://httpbin.org'
# #SSl����ʱ��
# context = ssl._create_unverified_context()
# re = urllib.request.urlopen(url,context=context)
# print(re.geturl())   # ��ַ
# print(re.getcode())  # ״̬��
# print(re.info())     # ����ҳ����Ϣ
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
        print(end='       ')   #ÿ���㷨����6������1����λ��������7��ռλ��
        for k in  range(1,i+1):
            print("%d*%d=%2d"%(k,i,k*i),end=' ')
            print("")#��ʽ����ͨ����while����ʽʵ��i=1while i<10:    k=1    while k<10-i:        print(end='       ')        k+=1    j = 1    while j<=i:        print("%d*%d=%2d"%(j,i,j*i),end=' ')        j+=1    print("")    i+=1 �����3. ����������#��ʽһ��ͨ����for..in..������ʵ��for i in range(9,0,-1): #������������9��ʼ��0����������-1    for j in range(1,i+1):         print("%d*%d=%2d"%(j,i,j*i),end=' ')    print("")#��ʽ����ͨ����while������ʵ��i=9while i>=1:    j = 1    while j<=i:        print("%d*%d=%2d"%(j,i,j*i),end=' ')        j+=1    print("")    i-=1�����4. ����������#��ʽһ��ͨ����for..in..������ʵ��for i in range(9,0,-1):    for j in range(1,i+1):         print("%d*%d=%2d"%(j,i,j*i),end=' ')    print("")    for k in range(i,10):         print(end='       ')#��ʽ����ͨ����while������ʵ��i=9while i>=1:    k=9    while k>i:        print(end='       ')        k-=1    j = 1    while j<=i:        print("%d*%d=%2d"%(j,i,j*i),end=' ')        j+=1    print("")    i-=1�����