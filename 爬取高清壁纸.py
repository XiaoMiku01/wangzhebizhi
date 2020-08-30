import urllib.request
from urllib.parse import unquote
import re
import os

def get_page(page):
    url_0 = 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page=' + str(
        page) + '&iOrder=0&iSortNumClose=1&jsoncallback=jQuery171092092645294628_1596033889782&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1596033890044'
    return url_0

# 获取所有1页所有信息  return 字符串html
def get_encry(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    page1 = urllib.request.Request(url,headers=headers)
    page2 = urllib.request.urlopen(page1)
    html = page2.read()
    return html


# 找到页面20个链接修改后缀    return 字典
def get_link(html):
    html = unquote(html.decode('utf-8'))
    html = html.replace('【嗨！我邀请你】','【嗨！我邀请】',1)
    a = html.find('sProdImgNo_8":"')
    name_link = {}
    name = []
    link = []

    name = re.compile('[\u4e00-\u9fa5]+-[\u4e00-\u9fa5]+|[\u4e00-\u9fa5]+[【][\u4e00-\u9fa5]+.[\u4e00-\u9fa5]+[】]|1:1等身雕塑·大乔|1:1等身雕塑·铠|[\u4e00-\u9fa5]+·[\u4e00-\u9fa5]+|[\u4e00-\u9fa5]+').findall(html)
    while a != -1:
        b = html.find('8.jpg', a, a + 255)
        if b != -1:
            link.append(html[a + 15:b + 9].replace('.jpg/200', '.jpg/0'))
        else:
            b = a + 9
        a = html.find('sProdImgNo_8":"', b)
    name_link = dict(zip(name, link))
    return name_link

# 创建总文件夹
def make_installer(folder=os.getcwd()+'\\壁纸'):
    os.mkdir(folder)
    os.chdir(folder)
    print('创建成功')
    pass


# 分类写入图片
def write_pic(name_link):
    global count
    for name , link  in name_link.items():
        f_name = str(name) + '.jpg'
        try:
            with open(f_name, 'wb') as f:
                f.write(get_encry(link))
                print('已成功下载%d张' % count)
                count += 1
        except FileNotFoundError:
            print('失败了')


def download (page):
    url_0 = get_page(page)
    html = get_encry(url_0)
    name_link = get_link(html)
    write_pic(name_link)

if __name__=='__main__':
    count = 1
    root = os.getcwd()+'\\壁纸'
    make_installer()
    for page in range(2):
        os.chdir(root)
        download(page)
    print('下载完成')
