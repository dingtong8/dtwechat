import json

import requests

from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Start.startDev import get_access_token


class AdvertisingDataAnalysis:
    """
    广告数据分析
    """
    def __init__(self):
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')

    def publisher_adpos_general(self, start, end):
        """
        获取公众号分广告位数据
        :return:
        """
        url_ = 'https://api.weixin.qq.com/publisher/stat?action=publisher_adpos_general&access_token={0}'.format(self.access_token)

        params = {
            "page": 1,
            "page_size": 10,
            "start_date": start,
            "end_date": end
        }
        ret_url_ = requests.get(url_, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_url_ = json.loads(ret_url_.text)
        print(ret_url_)

    def publisher_cps_general(self, start, end):
        """
        获取公众号分广告位数据
        :return:
        """
        url_ = 'https://api.weixin.qq.com/publisher/stat?action=publisher_adpos_general&access_token={0}'.format(self.access_token)

        params = {
            "page": 1,
            "page_size": 10,
            "start_date": start,
            "end_date": end
        }
        ret_url_ = requests.get(url_, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_url_ = json.loads(ret_url_.text)
        print(ret_url_)

    def publisher_settlement(self, start, end):
        """
        获取公众号结算收入数据及结算主体信息
        :return:
        """
        url_ = 'https://api.weixin.qq.com/publisher/stat?action=publisher_settlement&access_token={0}'.format(self.access_token)

        params = {
            "page": 1,
            "page_size": 10,
            "start_date": start,
            "end_date": end
        }
        ret_url_ = requests.get(url_, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_url_ = json.loads(ret_url_.text)
        print(ret_url_)



