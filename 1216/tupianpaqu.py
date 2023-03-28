import requests
from urllib import parse
from urllib import request
import os
import time
# https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=4&totalpage=0&page=0&iOrder=0&iSortNumClose=1&jsoncallback=jQuery17107759783510094294_1639613793990&iAMSActivityId=51991&_everyRead=true&iTypeId=1&iFlowId=267733&iActId=2735&iModuleId=2735&_=1639613794074
headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Mobile Safari/537.36'
}
def extract_images(data):
    image_urls=[]
    for i in range(1,9):
        image_url=parse.unquote(data['sProdImgNo_%d'%i]).replace("200","0")
        image_urls.append(image_url)
    # print(image_urls)
    return image_urls
def main():
    # 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=4&totalpage=0&page=1&iOrder=0&iSortNumClose=1&jsoncallback=jQuery17107759783510094294_1639613793990&iAMSActivityId=51991&_everyRead=true&iTypeId=1&iFlowId=267733&iActId=2735&iModuleId=2735&_=1639613794074'
    for page in range(2):
        page_url = f'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={page}&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1639614624669'
        resp = requests.get(page_url,headers=headers)
        #result=resp.text
        result=resp.json()
        #print(result)
        print(result['List'])
        data_list = result['List']
        # for index,data in enumerate(data_list):
        #     #print(data)
        #     # image_url=parse.unquote(data['sProdImgNo_8']).replace("200","0")
        #     # print(image_url)
        #     image_urls=extract_images(data)
        #     name = parse.unquote(data["sProdName"])
        #
        #     dirpath=os.path.join("images",name)  # 图片存储的路径
        #     if not os.path.exists(dirpath):
        #         os.mkdir(dirpath)          # mkdir("images/%s"%name)
        #     #print(name)
        #     #break
        #     #存放当前的8张图片
        #     for index,image_url in enumerate(image_urls):
        #         request.urlretrieve(image_url,os.path.join(dirpath,"%d.jpg"%(index+1)))
        #         print("%s下载完成！"%image_url)
        # break
if __name__ == '__main__':
    main()