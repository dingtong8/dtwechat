import json

import requests

from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Start.startDev import get_access_token


class LongShortConvert:
    def __init__(self):
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')

    def gen_shorten(self, long_data, expire_seconds):
        url_shorten = 'https://api.weixin.qq.com/cgi-bin/shorten/gen?access_token={0}'.format(self.access_token)
        params = {
            "long_data": long_data,
            "expire_seconds": expire_seconds
        }
        ret_shorten = requests.post(url_shorten, params=params)
        ret_shorten = json.loads(ret_shorten.text)
        print(ret_shorten)

        return ret_shorten

    def fetch_shorten(self, short_key, expire_seconds):
        url_fetch = 'https://api.weixin.qq.com/cgi-bin/shorten/fetch?access_token={0}'.format(self.access_token)
        params = {
            "long_data": short_key,
            "expire_seconds": expire_seconds
        }
        ret_fetch = requests.post(url_fetch, params=params)
        ret_fetch = json.loads(ret_fetch.text)
        print(ret_fetch)

        return ret_fetch

