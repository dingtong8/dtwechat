import json
import requests

from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Start.startDev import get_access_token


class UserDataAnalysis:
    """
    用户分析
    """

    def __init__(self):
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')

    def getusersummary(self, start, end):
        """
        获取用户增减数据
        :return:
        """
        url_summary = 'https://api.weixin.qq.com/datacube/getusersummary?access_token={0}'.format(self.access_token)
        params = {
            "begin_date": start,
            "end_date": end
        }
        ret_summary = requests.post(url_summary, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_summary = json.loads(ret_summary.text)
        print(ret_summary)

    def getusercumulate(self, start, end):
        """
        获取累计用户数据
        :return:
        """
        url_cumulate = 'https://api.weixin.qq.com/datacube/getusercumulate?access_token={0}'.format(self.access_token)
        params = {
            "begin_date": start,
            "end_date": end
        }
        ret_cumulate = requests.post(url_cumulate, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_cumulate = json.loads(ret_cumulate.text)
        print(ret_cumulate)


