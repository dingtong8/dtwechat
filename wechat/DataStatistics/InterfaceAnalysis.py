import json

import requests

from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Start.startDev import get_access_token


class InternetSnalysis:
    def __init__(self):
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')

    def getinterfacesummary(self, start, end):
        url_get = 'https://api.weixin.qq.com/datacube/getinterfacesummary?access_token={0}'.format(self.access_token)
        params = {
            "begin_date": start,
            "end_date": end
        }
        ret_streammsg = requests.post(url_get, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_streammsg = json.loads(ret_streammsg.text)
        print(ret_streammsg)

    def getinterfacesummaryhour(self, start, end):
        url_get = 'https://api.weixin.qq.com/datacube/getinterfacesummaryhour?access_token={0}'.format(self.access_token)
        params = {
            "begin_date": start,
            "end_date": end
        }
        ret_streammsg = requests.post(url_get, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_streammsg = json.loads(ret_streammsg.text)
        print(ret_streammsg)
