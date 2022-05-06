import datetime
import json
import os
import time
import urllib
import uuid

import requests
from django.http import JsonResponse
from django.test import TestCase
import requests
from PIL import Image
from io import BytesIO

# Create your tests here.
# aa = '2021-07-02 09:23:56.234022'
#
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1625217961)))
#
# print()

# aaa = {
#     'openid': 'oLiV45hlll9pxr3PG13DZxjtZHvc',
#     'nickname': 'DT',
#     'sex': 1,
#     'language': 'zh_CN',
#     'city': 'æ\xad¦æ±\x89',
#     'province': 'æ¹\x96å\x8c\x97',
#     'country': 'ä¸\xadå\x9b½',
#     'headimgurl': 'https://thirdwx.qlogo.cn/mmopen/vi_32'
#                   '/rSjh5X2dzsnU63lBKPyb1fI6Ted6O5pu18sibVMAquExiaO9ia3BJ8ubDVmNVUdPQdm2Toxsp8SFHibBmuwht4KIHw/132',
#     'privilege': []
# }
#
# print(aaa['province'])

# print(str(int(time.time())))

# data = {'code': 0, 'nonceStr': 'FevOCFWSGjaa1tNfvQMEiuh3NqvvnH8A', 'timestamp': '1625709783',
#       'signature': 'a191a1ca6f0524d9bb27e35e604259394f11e047', 'appId': 'wx8333db76f4523de2', 'message': ''}

# print(type(data))
# print(json.dumps(data))

# json_string = json.dumps(data)
# print(json_string)
#
# params = {'id': 100, 'name': '广东', 'count': 0}
# del params['count']
# params = {'tag': params}
#
# print(json.dumps(params, ensure_ascii=False))
# print(json.dumps(params, ensure_ascii=False).encode('utf-8'))

# params = {"user_list": []}
# openid_lst = ['oLiV45hlll9pxr3PG13DZxjtZHvc', 'batch_get_userinfo']
# for i in range(len(openid_lst)):
#     print(params['user_list'].append({"openid": openid_lst[i]}))
#     # params['user_list'][i] = {"openid": openid_lst[i]}
# print(params)
#
# total = 3399990
# if total > 10000:
#     aa = total / 10000  # 除
#     cc = total // 10000  # 取整
#     if aa != float('{0}.0'.format(cc)):
#         query_count = cc + 1  # 如果不能整除，查询次数就要 +1
#     else:
#         query_count = cc  # 如果能整除，查询次数不变
# else:
#     query_count = 1  # 果如粉丝小于等于10000，查询次数为 1
#
#
# next_openid = ''
# openid_lsts = []
# for i in range(query_count):
#     if i == 0:
#         print('next_openid', next_openid)
#         next_openid = i
#         openid_lsts.append(next_openid)
#     else:
#         next_openid = i
#         openid_lsts.append(next_openid)
#
#
# print(openid_lsts)
# from wechat.tools import GetRandomStr

# ticket = 'gQHm8DwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAyTVBsUTE2S0JkVUMxOGRGZk54MWQAAgQNHOhgAwQAjScA'
# getQRCode_url = 'https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket={0}'
# ret_getQRCode = requests.get(getQRCode_url.format(ticket))
#
# print(ret_getQRCode.content)

# print(os.path.join(os.getcwd(), r'wechat\AccountManage'))


# def write_fail_cmd(cmd):
#     with open('cmd_log.txt', mode='a', encoding='utf8') as f:
#         f.write("{0} {1}\n".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), str(cmd)))
#
#
# write_fail_cmd('cmd_cp')

# url = 'https://ss1.dydata.io/img_pdf/2026538069305462784-1.png'
# response = requests.get(url)
# image = Image.open(BytesIO(response.content))
# print(image)
# image.save(r'D:\Code\dtwechat\wechat\tests.jpg')
imgpath = r'D:\Code\dtwechat\wechat\Message\png\91303d33c6812bf38226107c915f1cf.jpg'
with open(imgpath, 'rb') as f:
    print(f.write(file))

