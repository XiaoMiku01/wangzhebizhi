import requests
import json
headers = {
    'cookie':'pgv_pvi=7809655808; RK=0pAB3sd5EL; ptcz=04e70eea5455e09b7b5b9ed8ac70cdedb4e517496512ec1f51b44c753546c438; pgv_pvid=9015247256; eas_sid=MTOkmpDiP8vXXEKwmNgWPrFT6S; LW_uid=B1b5g7S57753b3i4A7P46716u9; tvfe_boss_uuid=8b76fe6048c38113; Qs_lvt_323937=1578387807; Qs_pv_323937=4192648618867519500; _ga=GA1.2.945724414.1578387808; uin_cookie=o1561900932; ied_qq=o1561900932; o_cookie=1561900932; pac_uid=1_1561900932; XWINDEXGREY=0; iip=0; luin=o1561900932; lskey=000100007217120ff5411790737d2cc8544d400cf4351e2af11f625227e6121e17b545509e21a81cbcaae872; LW_sid=x1n519E6m7y1l9x4y7m3b8i5m6; pgv_si=s5397497856; pgv_info=ssid=9015247256; tokenParams=%3Ftid%3D475140; _qpsvr_localtk=0.7352495172867499; tgl_sid=597250876df23d7ae87ecea2e42e8604e685d83b; tglLoginType=qq; login_type=qqpc; qq=1561900932; acctype=qc; access_token=5F618709FDEDA52BBFF12E56478291C4; openid=CE07FE66497B7690E9CA5C58765C880A; appid=101492244; pvpqqcomrouteLine=index_newsdetail_a20190620material_a20190620material_a20190620material_a20190620material',
    'user-agent':'pgv_pvi=7809655808; RK=0pAB3sd5EL; ptcz=04e70eea5455e09b7b5b9ed8ac70cdedb4e517496512ec1f51b44c753546c438; pgv_pvid=9015247256; eas_sid=MTOkmpDiP8vXXEKwmNgWPrFT6S; LW_uid=B1b5g7S57753b3i4A7P46716u9; tvfe_boss_uuid=8b76fe6048c38113; Qs_lvt_323937=1578387807; Qs_pv_323937=4192648618867519500; _ga=GA1.2.945724414.1578387808; uin_cookie=o1561900932; ied_qq=o1561900932; o_cookie=1561900932; pac_uid=1_1561900932; XWINDEXGREY=0; iip=0; luin=o1561900932; lskey=000100007217120ff5411790737d2cc8544d400cf4351e2af11f625227e6121e17b545509e21a81cbcaae872; LW_sid=x1n519E6m7y1l9x4y7m3b8i5m6; pgv_si=s5397497856; tokenParams=%3Ftid%3D475140; _qpsvr_localtk=0.7352495172867499; pgv_info=ssid=9015247256&pgvReferrer=; skey=@3qDdEtTIh; rv2=80218C25EB650EFECF5E346219AE6988FB8F7C62087A4F5A0D; property20=B53EAA8AE69DC29AAD6CE06504303137F08A89FC760AD51DB3C69743754842B08D3F077F042FE741; pvpqqcomrouteLine=index_newsdetail_a20190620material_a20190620material_a20190620material_a20190620material_a20190620material; tgl_sid=ed9e30fdff2aec9e4f17a659f8dd10de28d9262d; tglLoginType=qq; login_type=qqpc; qq=1561900932; acctype=qc; access_token=5F618709FDEDA52BBFF12E56478291C4; openid=CE07FE66497B7690E9CA5C58765C880A; appid=101492244'}
url = 'https://api.material.qq.com/material/list?pageIndex=1&pageSize=15&tag[]=k10&searchText='
#url = 'https://api.material.qq.com/material/download?mId={}%3D%3D'.format('hEkgriF6yungdb2oq26biA')
#url = 'https://pvp.qq.com/sucai/#/list'
re = requests.get(url=url,headers=headers)
print(re.text)
n_re = json.loads(re.text)

print(n_re)
#print(n_re['data']['url'])
# q = n_re['data']['data']
#
# for each in q:
#     with open("h1.txt",'wb') as f:
#         f.write(each['id']+'\t\t'+each['title']+'\t\t'+each['format']+'\n')
