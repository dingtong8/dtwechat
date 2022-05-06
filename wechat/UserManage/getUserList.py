import json
import requests

from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Start.startDev import get_access_token


class UserManage:
    """
    用户管理
    """
    def __init__(self):
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')

    def get_user_lst(self):
        """
        获取用户列表
        :return:
        """
        url_get = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token={0}'.format(self.access_token)
        ret_get = requests.get(url_get)
        ret_get = json.loads(ret_get.text)
        total = ret_get['total']

        if total > 10000:
            aa = total / 10000      # 除
            cc = total // 10000     # 取整
            if aa != float('{0}.0'.format(cc)):
                query_count = cc + 1    # 如果不能整除，查询次数就要 +1
            else:
                query_count = cc        # 如果能整除，查询次数不变
        else:
            query_count = 1     # 果如粉丝小于等于10000，查询次数为 1

        next_openid = ''
        openid_lsts = []
        for i in range(query_count):
            if i == 0:
                url_get = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token={0}'.format(self.access_token)
                ret_get = requests.get(url_get)
                ret_get = json.loads(ret_get.text)
                next_openid = ret_get['next_openid']
                openid_lst = ret_get['data']['openid']
                openid_lsts.append(openid_lst)
            else:
                url_get = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token={0}&next_openid={1}'.format(self.access_token, next_openid)
                ret_get = requests.get(url_get)
                ret_get = json.loads(ret_get.text)
                next_openid = ret_get['next_openid']
                openid_lst = ret_get['data']['openid']
                openid_lsts.append(openid_lst)

        print('所有用户：', openid_lsts)
        return openid_lsts


