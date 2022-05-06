import json

import requests

from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Start.startDev import get_access_token


class LabelManage:
    """
    用户标签管理
    参考：https://developers.weixin.qq.com/doc/offiaccount/User_Management/User_Tag_Management.html
    """

    def __init__(self):
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')

    def create_label(self, label_lst):
        """
        创建标签
        :param label_lst:
        :return:
        """
        url_create = 'https://api.weixin.qq.com/cgi-bin/tags/create?access_token={0}'.format(self.access_token)

        for i in label_lst:
            params = {
                "tag": {"name": "{0}".format(i)}
            }

            ret_url_create = requests.post(url_create, json.dumps(params, ensure_ascii=False).encode('utf-8'))
            ret_url_create = json.loads(ret_url_create.text)
            print(ret_url_create)

    def get_label(self):
        """
        获取公众号已创建的标签
        :return:
        """
        url_get = 'https://api.weixin.qq.com/cgi-bin/tags/get?access_token={0}'.format(self.access_token)
        ret_select_menu = requests.get(url_get, timeout=3)
        ret_select_menu = json.loads(ret_select_menu.text)
        print(ret_select_menu)

        return ret_select_menu

    def modify_label(self, old_label, new_label):
        """
        编辑标签
        :param old_label:
        :param new_label:
        :return:
        """
        url_modify = 'https://api.weixin.qq.com/cgi-bin/tags/update?access_token={0}'.format(self.access_token)

        old_label_lst = self.get_label()['tags']
        for i in old_label_lst:
            if i['name'] == old_label:
                params = i
                del params['count']
                params = {'tag': params}
                if params['tag']['name'] != new_label:
                    print(params)
                    print(json.dumps(params, ensure_ascii=False).encode('utf-8'))
                    ret_modify_label = requests.post(url_modify, json.dumps(params, ensure_ascii=False).encode('utf-8'))
                    ret_modify_label = json.loads(ret_modify_label.text)
                    print(ret_modify_label)
                else:
                    print('新旧标签一样，请换一个标签名')
            else:
                print('该组标签无需修改', i)
                continue

    def del_label(self, label):
        """
        删除标签
        :param label:
        :return:
        """
        url_del = 'https://api.weixin.qq.com/cgi-bin/tags/delete?access_token={0}'.format(self.access_token)

        label_lst = self.get_label()['tags']
        for i in label_lst:
            if label == i['name']:
                label_id = i['id']
                params = {"tag": {"id": "{0}".format(label_id)}}
                ret_del_label = requests.post(url_del, json.dumps(params, ensure_ascii=False).encode('utf-8'))
                ret_del_label = json.loads(ret_del_label.text)
                print(ret_del_label)
            else:
                print('该组标签无需删除', i)
                continue

    def get_label_fans(self, label):
        """
        获取标签下粉丝列表
        :param label:
        :return:
        """
        get_url = 'https://api.weixin.qq.com/cgi-bin/user/tag/get?access_token={0}'.format(self.access_token)

        label_lst = self.get_label()['tags']
        for i in label_lst:
            if label == i['name']:
                label_id = i['id']
                params = {"tagid": "{0}".format(label_id), "next_openid": ""}
                print(params)
                ret_get_url = requests.post(get_url, json.dumps(params, ensure_ascii=False).encode('utf-8'))
                ret_get_url = json.loads(ret_get_url.text)
                print(ret_get_url)
            else:
                print('该组标签不合需要', i)
                continue

    def batch_set_fan_label(self, openid_list, label):
        """
        批量为用户打标签
        :param openid_list: 用户 openid 列表
        :param label: 标签名
        :return:
        """
        url_batch_label = 'https://api.weixin.qq.com/cgi-bin/tags/members/batchuntagging?access_token={0}'.format(
            self.access_token)

        label_lst = self.get_label()['tags']
        for i in label_lst:
            if label == i['name']:
                label_id = i['id']
                params = {
                    "openid_list": openid_list,
                    "tagid": label_id
                }
                print(params)
                ret_batch_label = requests.post(url_batch_label, json.dumps(params, ensure_ascii=False).encode('utf-8'))
                ret_batch_label = json.loads(ret_batch_label.text)
                print(ret_batch_label)
            else:
                print('该组标签不合需要', i)
                continue

    def batch_unset_fan_label(self, openid_list, label):
        """
        批量为用户取消标签
        :param openid_list: 用户 openid 列表
        :param label: 标签名
        :return:
        """
        url_batch_label = 'https://api.weixin.qq.com/cgi-bin/tags/members/batchuntagging?access_token={0}'.format(
            self.access_token)

        label_lst = self.get_label()['tags']
        for i in label_lst:
            if label == i['name']:
                label_id = i['id']
                params = {
                    "openid_list": openid_list,
                    "tagid": label_id
                }
                ret_batch_unset_label = requests.post(url_batch_label,
                                                      json.dumps(params, ensure_ascii=False).encode('utf-8'))
                ret_batch_unset_label = json.loads(ret_batch_unset_label.text)
                print(ret_batch_unset_label)
            else:
                print('该组标签不合需要', i)
                continue

    def get_fan_labels(self, openid_list):
        """
        获取用户身上的标签列表
        :param openid_list:
        :return:
        """
        url_get = 'https://api.weixin.qq.com/cgi-bin/tags/getidlist?access_token={0}'.format(self.access_token)

        for i in openid_list:
            params = {"openid": i}
            ret_fan_labels = requests.post(url_get,
                                           json.dumps(params, ensure_ascii=False).encode('utf-8'))
            ret_fan_labels = json.loads(ret_fan_labels.text)
            print(ret_fan_labels)

