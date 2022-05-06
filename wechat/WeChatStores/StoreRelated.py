import json

import requests

from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Start.startDev import get_access_token


class StoreRelated:
    def __init__(self):
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')

    def uploadimg(self, imgpath):
        url = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token={0}'.format(self.access_token)

        with open(imgpath, 'rb') as f:
            fileStream = f.read()

        params = {
            "buffer": fileStream
        }

        ret_url = requests.post(url, params=params)
        ret_url = json.loads(ret_url.text)
        print(ret_url)

    def create_store(self):
        url = 'http://api.weixin.qq.com/cgi-bin/poi/addpoi?access_token={0}'.format(self.access_token)

        params = {
            "business": {
                "base_info": {
                    "sid": "33788392",
                    "business_name": "15个汉字或30个英文字符内",
                    "branch_name": "不超过10个字，不能含有括号和特殊字符",
                    "province": "不超过10个字",
                    "city": "不超过30个字",
                    "district": "不超过10个字",
                    "address": "门店所在的详细街道地址（不要填写省市信息）：不超过80个字",
                    "telephone": "不超53个字符（不可以出现文字）",
                    "categories": ["美食,小吃快餐"],
                    "offset_type": 1,
                    "longitude": 115.32375,
                    "latitude": 25.097486,
                    "photo_list": [{"photo_url": "https:// 不超过20张.com"}, {"photo_url": "https://XXX.com"}],
                    "recommend": "不超过200字。麦辣鸡腿堡套餐，麦乐鸡，全家桶",
                    "special": "不超过200字。免费wifi，外卖服务",
                    "introduction": "不超过300字。麦当劳是全球大型跨国连锁餐厅，1940 年创立于美国，在世界上大约拥有3 万间分店。主要售卖汉堡包，以及薯条、炸鸡、汽水、冰品、沙拉、 水果等快餐食品",
                    "open_time": "8:00-20:00",
                    "avg_price": 35
                }
            }
        }

        ret_url = requests.post(url, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_url = json.loads(ret_url.text)
        print(ret_url)

    def store_category(self):
        url = 'http://api.weixin.qq.com/cgi-bin/poi/getwxcategory?access_token={0}'.format(self.access_token)

        ret_url = requests.get(url)
        ret_url = json.loads(ret_url.text)
        print(ret_url)

    def get_province(self):
        url = 'https://api.weixin.qq.com/wxa/get_district?access_token={0}'.format(self.access_token)

        ret_url = requests.get(url)
        ret_url = json.loads(ret_url.text)
        print(ret_url)



