# utlls.py
import requests

# 得到原始用户信息数据
def getUserInfo(userId):
    '''
    input:
        userid  # AI Studio用户id
    output:
    '''
    url = 'https://aistudio.baidu.com/studio/user/center/public/info/'

    headers = {
        'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
        'Cookie': 'BIDUPSID=DCA5C6F2C2B97924AB7C3E967B206291; PSTM=1615713661; __yjs_duid=1_0037114dcb210f1a40ba2da3d23171701618733030270; BAIDUID=73701ADEFCAFE0F247B4A36BEC059212:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=8B78FD27644F083B887EA43A14D9BA51:FG=1; ai-studio-ticket=99191E107E524D37A173AD33516D479C1C454F31B1664224AA697C24C1A869B9; Hm_lvt_8b973192450250dd85b9011320b455ba=1639739753,1639822113,1639828536,1639904884; BDUSS=NLUUVNSGdKYTdzc2MtcjNKZDVDZ3dCbnY4SDRCVG9Jenh3TlFrN281eURnLVpoSUFBQUFBJCQAAAAAAAAAAAEAAADsDfNKbXp6bnFfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIP2vmGD9r5haz; BDUSS_BFESS=NLUUVNSGdKYTdzc2MtcjNKZDVDZ3dCbnY4SDRCVG9Jenh3TlFrN281eURnLVpoSUFBQUFBJCQAAAAAAAAAAAEAAADsDfNKbXp6bnFfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIP2vmGD9r5haz; Hm_lpvt_8b973192450250dd85b9011320b455ba=1639904902; H_PS_PSSID=34446_35298_35104_31660_34584_35491_35315_26350; delPer=0; PSINO=3; BA_HECTOR=8k8k04002h8k0h04ut1grttv40r; ab_sr=1.0.1_ZDEzZTg1ZGY4NWE3M2JmNDUxNjJhODlkNmJiYTdiZTcwY2YzN2ExZGNmOGM5MGVjODk0ZjliZWYzMzNjMGE5ODVlYTRjY2UwOTk0OGFmMGY4OGY2NDE1ZTNjMDE0OTk4NjFlNTZhNGVlMjJkY2JjYjUxZDI5OTA5ZTFmYzg5ODJlM2NhODkwNThmMzFjMTUxOTJlY2I2MjA4YjUxNzBkODEwODY4NDA0ZWVkMDRlZmY5OTYxODU5ZjM2ODllNzdm; __yjs_st=2_MmI4MjM5ZmQ2M2YzOTAzNzdiNTEwYWJlMzUwMjViMWU0N2ExNDg1ODdhNjk3ZTFiMTBhZWIyZDcxYjA0YWZlNmJjZmZjNjU5YjkzYmUwMjRhZGM5NmVlN2NjYzc0MjA5MWU1YTkxYjRlOWZhZDZkMWE5MmRhY2NjZmE5NDI1ZmEwY2E5YTQ2NGJiNjI1MTMyYWUzOTJlNmY1Y2E2Y2Y2ZmM4YzNiMzQxNmFjOWIxYzFjZGRmNmM5OTFkOTU3NTY0OGM4Y2JiZTNkYWJlMDhmMjA1YzlkOGVmYzM2ODU0MmRhMzc5ODk1YTEwMDRmODMxNTUyNDcxZDE2YjhkOGY2NV83X2YxOTM3MDRm; RT="z=1&dm=baidu.com&si=ap4s4rc7hp7&ss=kxd10yfu&sl=1f&tt=gag&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=9v6z&cl=299n&ul=a8mk"'
    }
    datas = {'userId': userId}
    res = requests.post(url, data=datas, headers=headers)
    return res

# 得到原始用户项目列表数据
def getProjectList(datas):
    url = 'https://aistudio.baidu.com/studio/user/center/project/shared'
    headers = {
        'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
        'Cookie': 'BIDUPSID=DCA5C6F2C2B97924AB7C3E967B206291; PSTM=1615713661; __yjs_duid=1_0037114dcb210f1a40ba2da3d23171701618733030270; BAIDUID=73701ADEFCAFE0F247B4A36BEC059212:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=8B78FD27644F083B887EA43A14D9BA51:FG=1; ai-studio-ticket=99191E107E524D37A173AD33516D479C1C454F31B1664224AA697C24C1A869B9; Hm_lvt_8b973192450250dd85b9011320b455ba=1639739753,1639822113,1639828536,1639904884; BDUSS=NLUUVNSGdKYTdzc2MtcjNKZDVDZ3dCbnY4SDRCVG9Jenh3TlFrN281eURnLVpoSUFBQUFBJCQAAAAAAAAAAAEAAADsDfNKbXp6bnFfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIP2vmGD9r5haz; BDUSS_BFESS=NLUUVNSGdKYTdzc2MtcjNKZDVDZ3dCbnY4SDRCVG9Jenh3TlFrN281eURnLVpoSUFBQUFBJCQAAAAAAAAAAAEAAADsDfNKbXp6bnFfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIP2vmGD9r5haz; Hm_lpvt_8b973192450250dd85b9011320b455ba=1639904902; H_PS_PSSID=34446_35298_35104_31660_34584_35491_35315_26350; delPer=0; PSINO=3; BA_HECTOR=8k8k04002h8k0h04ut1grttv40r; ab_sr=1.0.1_ZDEzZTg1ZGY4NWE3M2JmNDUxNjJhODlkNmJiYTdiZTcwY2YzN2ExZGNmOGM5MGVjODk0ZjliZWYzMzNjMGE5ODVlYTRjY2UwOTk0OGFmMGY4OGY2NDE1ZTNjMDE0OTk4NjFlNTZhNGVlMjJkY2JjYjUxZDI5OTA5ZTFmYzg5ODJlM2NhODkwNThmMzFjMTUxOTJlY2I2MjA4YjUxNzBkODEwODY4NDA0ZWVkMDRlZmY5OTYxODU5ZjM2ODllNzdm; __yjs_st=2_MmI4MjM5ZmQ2M2YzOTAzNzdiNTEwYWJlMzUwMjViMWU0N2ExNDg1ODdhNjk3ZTFiMTBhZWIyZDcxYjA0YWZlNmJjZmZjNjU5YjkzYmUwMjRhZGM5NmVlN2NjYzc0MjA5MWU1YTkxYjRlOWZhZDZkMWE5MmRhY2NjZmE5NDI1ZmEwY2E5YTQ2NGJiNjI1MTMyYWUzOTJlNmY1Y2E2Y2Y2ZmM4YzNiMzQxNmFjOWIxYzFjZGRmNmM5OTFkOTU3NTY0OGM4Y2JiZTNkYWJlMDhmMjA1YzlkOGVmYzM2ODU0MmRhMzc5ODk1YTEwMDRmODMxNTUyNDcxZDE2YjhkOGY2NV83X2YxOTM3MDRm; RT="z=1&dm=baidu.com&si=ap4s4rc7hp7&ss=kxd10yfu&sl=1f&tt=gag&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=9v6z&cl=299n&ul=a8mk"',
        'x-studio-token': '36FB992214492F7A593569FD2ED2429FA63A894A0FC29D0C49757F7EAEE3B58D682BB2CA2A9A219E86D3602552E332B5F3F47AEC8008A63DE064C1278F6968EBCBF69DC2BF8137AEB6034E7AE7CEDF47'
    }
    res = requests.post(url, json=datas, headers=headers)
    return res

# 得到用户个人信息中的有用信息
def getInfoRes(userId):
    res = getUserInfo(userId)
    result = res.json().get('result')
    # print(result)
    # 签名
    absInfo = result.get('abs')
    # 头像url
    portrait = result.get('portrait')
    # nickname
    nickname = result.get('nickname')
    # 关注数
    followeeCount = result.get('followeeCount')
    # 粉丝数
    followerCount = result.get('followerCount')
    # 加入天数
    joinDays = result.get('joinDays')
    # 战力值
    totalUserPoints = result.get('totalUserPoints')
    # 用户省份
    userLocationProvince = result.get('userLocationProvince')
    # 用户城市
    userLocationCity = result.get('userLocationCity')

    return absInfo, portrait, nickname, followeeCount, followerCount, joinDays, totalUserPoints, userLocationProvince, userLocationCity


def run1(userId=118783):
    res = getInfoRes(userId)
    return res


def run2(userId=118783):
    datas = {'p': 1, 'pageSize': 10, 'topic': 0, 'category': 0, 'tags': [], 'order': 0, 'kw': "", 'type': 1,
             'userId': userId}
    res = getProjectList(datas)
    result = res.json().get('result')
    totalPage = result.get('totalPage')
    projectList = []
    for p in range(1, totalPage + 1):
        datas = {'p': p, 'pageSize': 10, 'topic': 0, 'category': 0, 'tags': [], 'order': 0, 'kw': "", 'type': 1,
                 'userId': userId}
        res = getProjectList(datas)
        result = res.json().get('result')
        data = result.get('data')
        for data in data:
            projectList.append(data)
    return projectList


def getwigets(userId):
    projectList=run2(userId)
    widgets = []
    for projectList1 in projectList:
        url_prefix = 'https://aistudio.baidu.com/aistudio/projectdetail/'
        var = ["projectId", "projectName", "projectAbs"]
        projectId=url_prefix+str(projectList1["projectId"])
        projectList1["projectId"]=projectId
        msms={}
        for j in var:
            msms[j] = projectList1[j]
        widgets.append(msms)
    # print(widgets)
    return widgets

def main():
    # 得到有用的个人信息
    res1=run1(userId=118783)
    print('得到有用的个人信息:')
    print(res1)
    # 得到有用的项目列表信息
    res2=getwigets(userId=118783)
    print('得到有用的项目列表信息:')
    print(res2)


# main()
#    # 得到有用的项目列表信息
# res2=getwigets(userId=118783)
# print('得到有用的项目列表信息:')
# print(res2)
if __name__ == '__main__':

    main()

