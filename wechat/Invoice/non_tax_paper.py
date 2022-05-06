import json
import requests

from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Start.startDev import get_access_token


class WechatInvoice:
    """
    微信发票
    """
    def __init__(self):
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')

    def get_ticket(self):
        url_get_ticket = 'https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token={0}&type=wx_card'.format(self.access_token)

        ret_get_ticket = requests.get(url_get_ticket)
        ret_get_ticket = json.loads(ret_get_ticket.text)
        print(ret_get_ticket)

        return ret_get_ticket


