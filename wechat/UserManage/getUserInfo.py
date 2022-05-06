import json
import requests

from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Start.startDev import get_access_token


class GetInfo:
    """
    获取用户信息
    """

    def __init__(self):
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')

    def get_userinfo(self, openid):
        """
        获取用户基本信息
        :return:
        """
        url_get = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token={0}&openid={1}&lang=zh_CN'.format(
            self.access_token, openid)

        ret_get = requests.get(url_get)
        ret_get = json.loads(ret_get.text)
        print(ret_get)

    def batch_get_userinfo(self, openid_lst):
        url_batch_get = 'https://api.weixin.qq.com/cgi-bin/user/info/batchget?access_token={0}'.format(self.access_token)

        params = {"user_list": []}
        for i in range(len(openid_lst)):
            params['user_list'].append({"openid": openid_lst[i]})

        ret_batch_get = requests.post(url_batch_get, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_batch_get = json.loads(ret_batch_get.text)
        print(ret_batch_get)

