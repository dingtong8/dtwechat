import json

import requests

from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Start.startDev import get_access_token


class SemanticComprehensionPrs:
    """
    语义理解
    """

    def __init__(self):
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')
        self.appid = APP_ID

    def comprehension(self, openid):
        url = 'https://api.weixin.qq.com/semantic/semproxy/search?access_token={0}'.format(self.access_token)

        params = {
            "query": "查一下明天从北京到上海的南航机票",
            "city": "北京",
            "category": "flight",
            "appid": self.appid,
            "uid": openid
        }

        ret_url = requests.post(url, json=json.dumps(params))
        ret_url = json.loads(ret_url.text)
        print(ret_url)

        imgurl = 'http://mmbiz.qpic.cn/mmbiz_jpg/j9NURAy8VNAEvvFx9yucXcZhmoXxI60ibcRtlx5ypENpD24dDozAI6ps22pgdwwqVKatgsXzL8NTVqG9xAu2qpg/0'
        url_2 = 'https://api.weixin.qq.com/cv/ocr/idcard?img_url={0}&access_token={1}'.format(imgurl, self.access_token)

        ret_url_2 = requests.post(url_2)
        ret_url_2 = json.loads(ret_url_2.text)
        print(ret_url_2)




