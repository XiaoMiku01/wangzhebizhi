import requests
import json
import urllib.request
import os


def openurl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    page1 = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(page1)
    html = page.read()
    return html


def allskin():
    all_skin = []
    for index in hero_data():
        ename = index['ename']
        cname = index['cname']
        #  构建图片URL地址
        for skin in range(1, 8):
            url_0 = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(ename) + '/' + str(
                ename) + '-bigskin-' + str(skin) + '.jpg'
            all_skin.append(url_0)
    return all_skin


def hero_data(url='https://pvp.qq.com/web201605/js/herolist.json'):
    hero_list = requests.get(url)
    data_str = hero_list.text
    hero_data = json.loads(data_str)  # 英雄字典的列表
    return hero_data


def installer(folder='E:\\py编程\\王者荣耀爬皮肤\\王者荣耀'):
    os.mkdir(folder)
    os.chdir(folder)
    print('创建成功')


def saveall():
    installer()
    global count
    for each in allskin():
        fliename = each.split('/')[-1]
        with open(fliename, 'wb') as f:
            try:
                f.write(openurl(each))
                print('已成功下载%d张' % count)
                count += 1
            except BaseException:
                f.close()
                os.remove(fliename)


if __name__ == '__main__':
    count = 1
    saveall()
