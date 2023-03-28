'''
1,确定目标地址
2，查看源代码
3，每一个索要爬取的地址都有不一样的id
4，通过获取网页源代码，获取得到id位置，最后进入下载页面
5，下载数据

'''
import requests #模块发送请求
import re # 正则表达式
# 1，找到目标地址
url="https://www.ypppt.com/"
# 伪装请求报头
header={
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Mobile Safari/537.36"
}
# 2,请求地址源代码
resp = requests.get(url,headers=header)
resp.encoding='utf-8'
#print(resp) #Resqonse [200] 代表返回成功
#print(resp.text)

#正则表达式 re 提取数据（id和名字）
#<a href="/article/2022/13541.html" class="p-title" target="_blank">大理石纹理极简商务PPT模板</a>
ppt_info=re.findall('<a href="(.*?)" class="p-title" target="_blank">(.*?)</a>',resp.text)
#print(ppt_info)

# 循环遍历 for
for index,title in ppt_info:
    ppt_id = index.split('/')[3][:5]
    # print(title,ppt_id)
    #将url补全
    index_url = 'https://www.ypppt.com/p/d.php?aid='+ppt_id
    # print(index_url)

    # 发送请求 备用下载
    resp_1 = requests.get(index_url,headers=header)

    download_url=re.findall('<li><a href="(.*?)">下载地址1</a></li>',resp_1.text) # 如果不使用for循环遍历下载这个列表的画需要加[0]且使用代码后面的方法。
    #print(download_url)

# content (.zip 音频 视频  图片） text（文本）
    for i in download_url:
        ppt_content = requests.get(i,headers=header).content
        with open('素材3\\' + title + '.zip', 'wb') as f:
            f.write(ppt_content)
        print(title, ppt_id + "下载成功！")
    # print(resp_1.text)
    # break

    # 保存数据 下载数据
    # ppt_content = requests.get(download_url, headers=header).content
    # with open('素材3\\' + title + '.zip', 'wb') as f:
    #     f.write(ppt_content)
    # print(title, ppt_id)