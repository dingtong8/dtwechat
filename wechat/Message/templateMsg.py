import json
import requests

from wechat.Menu.menu_constants import industry_params01, template_id_short_params01, template_id_params01, \
    send_template_msg_params01
from wechat.Start.startDev import get_access_token
from dtwechat.settings import APP_ID, APP_SECRET


class TemplateMsg:
    """
    模板消息仅用于公众号向用户发送重要的服务通知
    需要选择公众账号服务所处的2个行业，每月可更改1次所选行业
    参考：https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Template_Message_Interface.html#5
    参考：https://blog.csdn.net/a816120/article/details/107233868
    模板消息规范：https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Template_Message_Operation_Specifications.html
    1 设置所属行业
    2 获取设置的行业信息
    3 获得模板ID
    4 获取模板列表
    5 删除模板
    6 发送模板消息
    7 事件推送
    """
    def __init__(self):
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')

    def set_industry(self):
        """设置所属行业"""
        url_set_industry = 'https://api.weixin.qq.com/cgi-bin/template/api_set_industry?access_token={0}'.format(self.access_token)

        params = industry_params01
        req_set_industry = requests.post(url_set_industry, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_set_industry = json.loads(req_set_industry.text)
        print(ret_set_industry)

        return ret_set_industry

    def get_industry(self):
        """获取设置的行业信息"""
        url_set_industry = 'https://api.weixin.qq.com/cgi-bin/template/get_industry?access_token={0}'.format(self.access_token)

        ret_get_industry = requests.get(url_set_industry, timeout=3)
        print(ret_get_industry.text)

        return ret_get_industry.text

    def get_template_id(self):
        """
        获得模板ID
        模板里的值有value和color两个，指的是keyword.DATA的内容和文字颜色。
        运输单信息
        {{first.DATA}}
        运输单号为：{{keyword1.DATA}}
        工程名称为：{{keyword2.DATA}}
        {{remark.DATA}}
        :return: 模板ID h5aQ_kyNDYz6oqqX47Len861PuqVZxnBDIMLjvPHpNE
        """
        url_get_template_id = 'https://api.weixin.qq.com/cgi-bin/template/api_add_template?access_token={0}'.format(self.access_token)

        params = template_id_short_params01
        req_set_industry = requests.post(url_get_template_id, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_set_industry = json.loads(req_set_industry.text)
        print(ret_set_industry)

        return ret_set_industry

    def get_template_list(self):
        """
        获取模板列表
        :return:
        """
        url_get_template_list = 'https://api.weixin.qq.com/cgi-bin/template/get_all_private_template?access_token={0}'.format(self.access_token)

        req_get_template_list = requests.get(url_get_template_list, timeout=3)
        ret_get_template_list = req_get_template_list.text
        print(ret_get_template_list)

        return ret_get_template_list

    def delete_template(self):
        """
        删除模板
        :return:
        """
        url_delete_template = 'https://api.weixin.qq.com/cgi-bin/template/del_private_template?access_token={0}'.format(
            self.access_token)

        params = template_id_params01
        req_delete_template = requests.post(url_delete_template, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_delete_template = json.loads(req_delete_template.text)
        print(ret_delete_template)

        return ret_delete_template

    def send_template_msg(self):
        """
        发送模板消息
        :return:
        """
        url_send_template_msg = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={0}'.format(
            self.access_token)

        params = send_template_msg_params01
        req_send_template_msg = requests.post(url_send_template_msg, json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_send_template_msg = json.loads(req_send_template_msg.text)
        print(ret_send_template_msg)

        return ret_send_template_msg

