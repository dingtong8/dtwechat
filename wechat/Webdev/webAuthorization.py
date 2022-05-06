import datetime
import json

import requests

from dtwechat.settings import APP_ID, APP_SECRET
from wechat.models import WechatWeb


class WEBAuthorization:
    """
    参考：https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/Wechat_webpage_authorization.html
    """
    def __init__(self):
        self.appid = APP_ID
        self.secret = APP_SECRET
        self.redirect_url = 'http://f4827s.natappfree.cc/wx/index/'
        self.response_type = 'code'
        self.scope = ['snsapi_base', 'snsapi_userinfo']
        self.state = 'STATE'
        self.grant_type = ['authorization_code', 'refresh_token']

    def agree_getcode(self):
        """该步骤只能粉丝在微信里面访问"""
        url_agree_getcode = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid={0}&redirect_uri={' \
                            '1}&response_type={2}&scope={3}&state={4}#wechat_redirect'.format(self.appid,
                                                                                              self.redirect_url,
                                                                                              self.response_type,
                                                                                              self.scope[1], self.state)

        ret_agree_getcode = requests.get(url_agree_getcode)
        # ret_agree_getcode = json.loads(ret_agree_getcode.text)
        print(ret_agree_getcode.text)

    def code_to_token(self, code):
        """
        用户授权成功后取出 code，通过 code获取token
        :param code:
        :return:
        """
        url_code_to_token = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid={0}&secret={1}&code={' \
                            '2}&grant_type={3}'.format(self.appid, self.secret, code, self.grant_type[0])

        ret_code_to_token = requests.get(url_code_to_token)
        ret_code_to_token = json.loads(ret_code_to_token.text)
        print(ret_code_to_token)

    def refresh_token(self, refresh_token):
        """
        刷新网页 access_token
        :param refresh_token:
        :return:
        """
        url_refresh_token = 'https://api.weixin.qq.com/sns/oauth2/refresh_token?appid={0}&grant_type={' \
                            '1}&refresh_token={2}'.format(self.appid, self.grant_type[1], refresh_token)

        ret_refresh_token = requests.get(url_refresh_token)
        ret_refresh_token = json.loads(ret_refresh_token.text)
        print(ret_refresh_token)

    def pull_user_info(self, access_token, openid):
        """
        拉取用户信息
        :return:
        """
        url_pull_user_info = 'https://api.weixin.qq.com/sns/userinfo?access_token={0}&openid={1}&lang=zh_CN'.format(
            access_token, openid)

        ret_pull_user_info = requests.get(url_pull_user_info)
        ret_pull_user_info = json.loads(ret_pull_user_info.text)
        print(ret_pull_user_info)

        openid = ret_pull_user_info['openid']
        nickname = ret_pull_user_info['nickname']
        sex = ret_pull_user_info['sex']
        language = ret_pull_user_info['language']
        city = ret_pull_user_info['city']
        province = ret_pull_user_info['province']
        country = ret_pull_user_info['country']
        headimgurl = ret_pull_user_info['headimgurl']
        privilege = ret_pull_user_info['privilege']

        query_fan = WechatWeb.objects.filter(openid=openid)
        if query_fan:
            # 旧用户
            WechatWeb.objects.filter(openid=openid).update(CreateTime=datetime.datetime.now())
        else:
            # 新用户
            fans = WechatWeb(openid=openid,
                             nickname=nickname,
                             sex=sex,
                             language=language,
                             city=city,
                             province=province,
                             country=country,
                             headimgurl=headimgurl,
                             privilege=privilege)
            fans.save()

    def expires_inspect(self, access_token, openid):
        """
        检查网页 access_token 是否过期
        :param access_token:
        :param openid:
        :return:
        """
        url_expired_inspect = 'https://api.weixin.qq.com/sns/auth?access_token={0}&openid={1}'.format(access_token, openid)

        ret_expires_inspect = requests.get(url_expired_inspect)
        ret_expires_inspect = json.loads(ret_expires_inspect.text)
        print(ret_expires_inspect)

    def save_user_info(self):
        """
        保存用户信息到数据库
        :return:
        """


