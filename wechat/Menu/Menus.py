import json
import requests

from wechat.Menu.menu_constants import menu_params01
from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Start.startDev import get_access_token


class Menu(object):
    """
    创建菜单
    查询菜单，返回json
    删除菜单
    获取菜单配置
    """
    def __init__(self):
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')

    def create_wx_menu(self):
        """
        微信公众号自定义菜单：
        创建接口
        :return:
        """
        url_create_menu = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token={0}'.format(self.access_token)

        params = menu_params01
        create_menu = requests.post(url_create_menu, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_create_menu = json.loads(create_menu.text)
        print(ret_create_menu)

        return ret_create_menu

    def select_wx_menu(self):
        """
        查询接口
        :return:
        """
        url_select_menu = 'https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token={0}'.format(
            self.access_token)
        ret_select_menu = requests.get(url_select_menu, timeout=3)
        print(ret_select_menu.text)

        return ret_select_menu.text

    def delete_wx_menu(self):
        """
        删除接口，调用此接口会删除默认菜单及全部个性化菜单，删除操作执行之后24小时后生效，重新关注立即生效
        :return:
        """
        url_delete_menu = 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token={0}'.format(self.access_token)
        ret_delete_menu = requests.get(url_delete_menu, timeout=3)
        print(ret_delete_menu.text)

    def get_current_selfmenu_info(self):
        """
        获取自定义菜单配置接口
        :return:
        """
        url_menu_info = 'https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token={0}'.format(self.access_token)
        ret_delete_menu = requests.get(url_menu_info, timeout=3)
        print(ret_delete_menu.text)

