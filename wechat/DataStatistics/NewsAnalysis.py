import json
import requests

from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Start.startDev import get_access_token


class NewsDataAnalysis:
    """
    消息分析
    """
    def __init__(self):
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')

    def getupstreammsg(self, start, end):
        """
        获取消息发送概况数据
        :return:
        """
        url_streammsg = 'https://api.weixin.qq.com/datacube/getupstreammsg?access_token={0}'.format(self.access_token)
        params = {
            "begin_date": start,
            "end_date": end
        }
        ret_streammsg = requests.post(url_streammsg, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_streammsg = json.loads(ret_streammsg.text)
        print(ret_streammsg)

    def getupstreammsghour(self, start, end):
        """
        获取消息分送分时数据
        :return:
        """
        url_summary = 'https://api.weixin.qq.com/datacube/getupstreammsghour?access_token={0}'.format(self.access_token)
        params = {
            "begin_date": start,
            "end_date": end
        }
        ret_summary = requests.post(url_summary, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_summary = json.loads(ret_summary.text)
        print(ret_summary)

    def getupstreammsgweek(self, start, end):
        """
        获取消息发送周数据
        :return:
        """
        url_summary = 'https://api.weixin.qq.com/datacube/getupstreammsgweek?access_token={0}'.format(self.access_token)
        params = {
            "begin_date": start,
            "end_date": end
        }
        ret_summary = requests.post(url_summary, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_summary = json.loads(ret_summary.text)
        print(ret_summary)

    def getupstreammsgmonth(self, start, end):
        """
        获取消息发送月数据
        :return:
        """
        url_summary = 'https://api.weixin.qq.com/datacube/getupstreammsgmonth?access_token={0}'.format(self.access_token)
        params = {
            "begin_date": start,
            "end_date": end
        }
        ret_summary = requests.post(url_summary, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_summary = json.loads(ret_summary.text)
        print(ret_summary)

    def getupstreammsgdist(self, start, end):
        """
        获取消息发送分布数据
        :return:
        """
        url_summary = 'https://api.weixin.qq.com/datacube/getupstreammsgdist?access_token={0}'.format(self.access_token)
        params = {
            "begin_date": start,
            "end_date": end
        }
        ret_summary = requests.post(url_summary, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_summary = json.loads(ret_summary.text)
        print(ret_summary)

    def getupstreammsgdistweek(self, start, end):
        """
        获取消息发送分布周数据
        :return:
        """
        url_summary = 'https://api.weixin.qq.com/datacube/getupstreammsgdistweek?access_token={0}'.format(self.access_token)
        params = {
            "begin_date": start,
            "end_date": end
        }
        ret_summary = requests.post(url_summary, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_summary = json.loads(ret_summary.text)
        print(ret_summary)

    def getupstreammsgdistmonth(self, start, end):
        """
        获取消息发送分布月数据
        :return:
        """
        url_summary = 'https://api.weixin.qq.com/datacube/getupstreammsgdistmonth?access_token={0}'.format(self.access_token)
        params = {
            "begin_date": start,
            "end_date": end
        }
        ret_summary = requests.post(url_summary, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_summary = json.loads(ret_summary.text)
        print(ret_summary)


