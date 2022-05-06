import json

import requests

from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Start.startDev import get_access_token


class BlackListManage:
    def __init__(self):
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')

    def get_black_lst(self):
        """
        获取公众号的黑名单列表
        :return:
        """
        url_get = 'https://api.weixin.qq.com/cgi-bin/tags/members/getblacklist?access_token={0}'.format(
            self.access_token)

        params = {
            "begin_openid": ""
        }
        ret_batch_get = requests.post(url_get, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_batch_get = json.loads(ret_batch_get.text)
        print(ret_batch_get)

    def shielding_users(self, openid_list):
        url_shielding = 'https://api.weixin.qq.com/cgi-bin/tags/members/batchblacklist?access_token={0}'.format(
            self.access_token)

        params = {
            "openid_list": openid_list
        }

        ret_url_shielding = requests.post(url_shielding, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_url_shielding = json.loads(ret_url_shielding.text)
        print(ret_url_shielding)

    def cancel_shielding(self, openid_list):
        url_cancel = 'https://api.weixin.qq.com/cgi-bin/tags/members/batchunblacklist?access_token={0}'.format(
            self.access_token)

        params = {
            "openid_list": openid_list
        }

        ret_url_shielding = requests.post(url_cancel, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_url_shielding = json.loads(ret_url_shielding.text)
        print(ret_url_shielding)
