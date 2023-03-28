import requests
from urllib import request
from urllib import parse
import os
import time
headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}
def extract_images(data):
    image_list=[]
    for i in range(1,5):
        image_li = parse.unquote(data['sProdImgNo_%s'%i]).replace("200", "0")
        image_list.append(image_li)
    print(image_list)
    return image_list
def main():
    for page in range(0,2):
        page_url=f'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=4023&sVerifyCode=ABCD&sDataType=JSON&iListNum=9&totalpage=0&page={page}&iOrder=0&iSortNumClose=1&iAMSActivityId=337009&_everyRead=true&iStatus=1&iFlowId=711378&iActId=4023&iModuleId=4023&_=1639731323224'
        #print(page_url)
        resp = requests.get(page_url,headers=headers)
        # html = resp.text
        # print(html)
        html = resp.json()
        detail_list=html["List"]
        for index,data in enumerate(detail_list):
            # image_li = parse.unquote(data['sProdImgNo_8']).replace("200","0")
            # print(image_li)
            image_urls=extract_images(data)
            name = parse.unquote(data['iProdId'])
            dirpath = os.path.join("image2",name)
            if not os.path.exists(dirpath):
                os.mkdir(dirpath)
            for index,image_url in enumerate(image_urls):
                request.urlretrieve(image_url, os.path.join(dirpath, "%d.jpg" % (index + 1)))
                print("%s下载完成！" % image_url)
if __name__ == '__main__':
    main()
