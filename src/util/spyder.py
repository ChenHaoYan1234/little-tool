import os
import re
from urllib import error

import requests

def Find(url, A):
    List = []
    print('正在检测图片总数，请稍等.....')
    t = 0
    i = 1
    s = 0
    while t < 1000:
        Url = url + str(t)
        try:
            # 这里搞了下
            Result = A.get(Url, timeout=7, allow_redirects=False)
        except BaseException:
            t = t + 60
            continue
        else:
            result = Result.text
            pic_url = re.findall('"objURL":"(.*?)",',
                                 result, re.S)  # 先利用正则表达式找到图片url
            s += len(pic_url)
            if len(pic_url) == 0:
                break
            else:
                List.append(pic_url)
                t = t + 60
    return s,List


def dowmloadPicture(html: str, keyword: str, numPicture: int,saveDir:str):
    num = 0
    # t =0
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)  # 先利用正则表达式找到图片url
    for each in pic_url:
        try:
            if each is not None:
                pic = requests.get(each, timeout=7)
            else:
                continue
        except:
            continue
        else:
            string = f"{saveDir}\\{keyword}_{num}.jpg"
            fp = open(string, 'wb')
            fp.write(pic.content)
            fp.close()
            num += 1
        if num >= numPicture:
            return


def spyder(keyword: str,saveDir:str, numPicture: int):

    ##############################
    # 这里加了点
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Upgrade-Insecure-Requests': '1'
    }

    A = requests.Session()
    A.headers = headers

    url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + keyword + '&pn='

    # 这里搞了下
    count,List = Find(url, A)
    if(os.path.isdir(saveDir)):
        os.mkdir(saveDir)
    if(numPicture > count):
        numPicture = count
    t = 0
    tmp = url
    while t < numPicture:
        try:
            url = tmp + str(t)

            # 这里搞了下
            result = A.get(url, timeout=10, allow_redirects=False)
        except error.HTTPError as e:
            print('网络错误，请调整网络后重试')
            t = t + 60
        else:
            dowmloadPicture(result.text, keyword,numPicture,saveDir)
            t = t + 60
