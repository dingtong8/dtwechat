import json
import requests

from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Start.startDev import get_access_token


class GraphicDataAnalysis:
    """
    图文分析
    """

    def __init__(self):
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')

    def getarticlesummary(self, start, end):
        """
        获取图文群发每日数据
        :return:
        """
        url_summary = 'https://api.weixin.qq.com/datacube/getarticlesummary?access_token={0}'.format(self.access_token)
        params = {
            "begin_date": start,
            "end_date": end
        }
        ret_summary = requests.post(url_summary, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_summary = json.loads(ret_summary.text)
        print(ret_summary)

    def getarticletotal(self, start, end):
        """
        获取图文群发总数据
        :return:
        """
        url_total = 'https://api.weixin.qq.com/datacube/getarticletotal?access_token={0}'.format(self.access_token)
        params = {
            "begin_date": start,
            "end_date": end
        }
        ret_total = requests.post(url_total, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_total = json.loads(ret_total.text)
        print(ret_total)

    def getuserread(self, start, end):
        """
        获取图文统计数据
        :return:
        """
        url_read = 'https://api.weixin.qq.com/datacube/getuserread?access_token={0}'.format(self.access_token)
        params = {
            "begin_date": start,
            "end_date": end
        }
        ret_read = requests.post(url_read, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_read = json.loads(ret_read.text)
        print(ret_read)

    def getuserreadhour(self, start, end):
        """
        获取图文统计分时数据
        :return:
        """
        url_readhour = 'https://api.weixin.qq.com/datacube/getuserreadhour?access_token={0}'.format(self.access_token)
        params = {
            "begin_date": start,
            "end_date": end
        }
        ret_readhour = requests.post(url_readhour, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_readhour = json.loads(ret_readhour.text)
        print(ret_readhour)

    def getusershare(self, start, end):
        """
        获取图文分享转发数据
        :return:
        """
        url_share = 'https://api.weixin.qq.com/datacube/getusershare?access_token={0}'.format(self.access_token)
        params = {
            "begin_date": start,
            "end_date": end
        }
        ret_share = requests.post(url_share, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_share = json.loads(ret_share.text)
        print(ret_share)

    def getusersharehour(self, start, end):
        """
        获取图文分享转发分时数据
        :return:
        """
        url_sharehour = 'https://api.weixin.qq.com/datacube/getusersharehour?access_token={0}'.format(self.access_token)
        params = {
            "begin_date": start,
            "end_date": end
        }
        ret_sharehour = requests.post(url_sharehour, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_sharehour = json.loads(ret_sharehour.text)
        print(ret_sharehour)


