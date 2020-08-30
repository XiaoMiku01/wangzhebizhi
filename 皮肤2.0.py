import requests
from urllib.parse import unquote
import json
import re,os,time
headers = {
"cookie":"pgv_pvi=7809655808; RK=0pAB3sd5EL; ptcz=04e70eea5455e09b7b5b9ed8ac70cdedb4e517496512ec1f51b44c753546c438; pgv_pvid=9015247256; eas_sid=MTOkmpDiP8vXXEKwmNgWPrFT6S; LW_uid=B1b5g7S57753b3i4A7P46716u9; tvfe_boss_uuid=8b76fe6048c38113; Qs_lvt_323937=1578387807; Qs_pv_323937=4192648618867519500; _ga=GA1.2.945724414.1578387808; uin_cookie=o1561900932; ied_qq=o1561900932; o_cookie=1561900932; pac_uid=1_1561900932; ts_refer=www.baidu.com/link; ts_uid=4956115614; XWINDEXGREY=0; iip=0; luin=o1561900932; lskey=000100007217120ff5411790737d2cc8544d400cf4351e2af11f625227e6121e17b545509e21a81cbcaae872; tgl_sid=ed9e30fdff2aec9e4f17a659f8dd10de28d9262d; tglLoginType=qq; login_type=qqpc; qq=1561900932; LW_sid=H1j5e976F8A0P787S7N6x3x1C4; pgv_si=s170784768; pt2gguin=o1561900932; pgv_info=ssid=9015247256; pvpqqcomrouteLine=index_wallpaper",
"referer":"https://pvp.qq.com/web201605/wallpaper.shtml",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
}

class Wzry():
    count = 1
    def __init__(self):
        self.hearo_links = {}
        self.hearo_names = []
        self.names_url = 'https://pvp.qq.com/web201605/js/herolist.json'

    def get_res(self,url):
        res = requests.get(url=url,headers=headers)
        return res

    def get_hearo_names(self):
        h= self.get_res(self.names_url)
        h = json.loads(h.text)
        for i in range(0, len(h)):
            self.hearo_names.append(h[i]['cname'])

    def get_hearo_links(self,page):
        link_url = 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={}&iOrder=0&iSortNumClose=1&jsoncallback=jQuery17102866754597974741_1596807820438&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1596807911490'.format(
            int(page))
        res = self.get_res(link_url)
        p1 = re.compile('[(](.*)[)]')
        all_list = re.findall(p1,res.text)[0]
        all_list = json.loads(unquote(all_list))['List']
        for i in range(0, len(all_list)):
            if all_list[i]['sProdName'] in self.hearo_links.keys():
                all_list[i]['sProdName'] = all_list[i]['sProdName'] + '(2)'
            self.hearo_links[all_list[i]['sProdName']] = all_list[i]['sProdImgNo_6'].replace('/200', '/0')

    def save_image(self):
        tem = list(self.hearo_links.keys())
        for image_name,link in self.hearo_links.items():
            res = self.get_res(link)
            for hearo_name in self.hearo_names:
                if any(hearo_name in s for s in tem) and hearo_name in image_name:
                    try:
                        os.mkdir(hearo_name)
                        os.chdir(hearo_name)
                    except:
                        os.chdir(hearo_name)
                    image_name_r = re.sub('[\/:*?"<>|]', '', image_name)
                    with open(image_name_r+'.jpg','wb') as image:
                        image.write(res.content)
                        os.chdir('..')
                        print(image_name+'  完成'+',一共已下载{}张'.format(Wzry.count))
                        Wzry.count += 1
                        tem.remove(image_name)

        for each in tem:
           res = self.get_res(self.hearo_links[each])
           try:
               os.mkdir('其他')
               os.chdir('其他')
           except:
               os.chdir('其他')
           with open(each + '.jpg', 'wb') as image:
               image.write(res.content)
               os.chdir('..')
               print(each + '完成(其他)'+',一共已下载{}张'.format(Wzry.count))
               Wzry.count += 1
        tem = []
        self.hearo_links = {}

    def main(self,i):
        start = time.clock()
        try:
            os.mkdir('王者皮肤2.0（分类）')
            os.chdir('王者皮肤2.0（分类）')
        except:
            os.chdir('王者皮肤2.0（分类）')
        self.get_hearo_names()
        for page in range(0,i):
            self.get_hearo_links(21)
            self.save_image()
            if (page + 1 % 4 == 0):
                time.sleep(5)
        end = time.clock()
        print(start)
        print(end)
        print('一个耗时：'+str((end-start)//60)+'分钟'+str((end-start)%60)+'秒')


if __name__ == '__main__':
    a = Wzry()
    a.main(22)



