import json
import requests

from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Start.startDev import get_access_token


class ServiceNews:
    """
    客服帐号管理
    发消息
    """

    def __init__(self):
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')

    def add_service(self):
        url_add_service = 'https://api.weixin.qq.com/customservice/kfaccount/add?access_token={0}'.format(
            self.access_token)

        params = {
            "kf_account": "dt@gh_f12dfaf9483a",
            "nickname": "客服1",
            "password": "3629de16da0c3eb580f24eec581977e1"
        }

        ret_add_service = requests.post(url_add_service, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_add_service = json.loads(ret_add_service.text)
        print(ret_add_service)


