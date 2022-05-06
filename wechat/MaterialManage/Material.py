import json

import requests

from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Start.startDev import get_access_token


class MaterialCorrelation:
    def __init__(self):
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')

    def add_temporary(self, filelength, filetype):
        if filetype == 'image':
            url_add = 'https://api.weixin.qq.com/cgi-bin/media/upload?access_token={0}&type=image'.format(
                self.access_token)
            params = {'media': open('{}'.format(filelength), 'rb')}
            ret_url_add = requests.post(url_add, files=params)
            ret_url_add = json.loads(ret_url_add.content.decode())
            print(ret_url_add)

        if filetype == 'voice':
            url_add = 'https://api.weixin.qq.com/cgi-bin/media/upload?access_token={0}&type=voice'.format(
                self.access_token)
        if filetype == 'video':
            url_add = 'https://api.weixin.qq.com/cgi-bin/media/upload?access_token={0}&type=video'.format(
                self.access_token)
        if filetype == 'thumb':
            url_add = 'https://api.weixin.qq.com/cgi-bin/media/upload?access_token={0}&type=thumb'.format(
                self.access_token)
            params = {
                'media': open(filelength, 'rb')
            }
            ret_url_add = requests.post(url_add,
                                        json.dumps(params, ensure_ascii=False).encode('utf-8'))
            ret_url_add = json.loads(ret_url_add.text)
            print(ret_url_add)

        else:
            ret_url_add = False

        return ret_url_add

    def get_temporary(self, media_id, filetype):
        url_get = 'https://api.weixin.qq.com/cgi-bin/media/get?access_token={0}&media_id={1}'.format(self.access_token,
                                                                                                     media_id)

        ret_url_get = requests.get(url_get)

        if filetype == 'image':
            ret_img = ret_url_get.content
            print(ret_img)
            with open('./a.jpg', 'wb') as f:
                f.write(ret_img)

        return ret_url_get

    def add_permanent(self):
        pass

    def get_permanent(self):
        pass

    def del_permanent(self):
        pass

    def modify_permanent_img_text(self):
        pass

    def get_material_total(self):
        url_get = 'https://api.weixin.qq.com/cgi-bin/material/get_materialcount?access_token={0}'.format(
            self.access_token)
        ret_url_get = requests.get(url_get)
        ret_url_get = json.loads(ret_url_get.text)
        print(ret_url_get)

        return ret_url_get

    def get_material_list(self, filetype, offset, count):
        url_get = 'https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token={0}'.format(
            self.access_token)

        params = {
            "type": filetype,
            "offset": offset,
            "count": count
        }
        ret_url_get = requests.post(url_get,
                                    json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_url_get = json.loads(ret_url_get.text)
        print(ret_url_get)

        return ret_url_get
