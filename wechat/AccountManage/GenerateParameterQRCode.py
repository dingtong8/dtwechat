import json
import os
import requests

from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Start.startDev import get_access_token
from wechat.tools import GetRandomStr


class CreateQRcode:
    """
    生成带参数的二维码
    临时二维码, 生成后的30天（即2592000秒）后过期
    永久二维码, 无过期时间, 最多10万个
    """

    def __init__(self):
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')
        self.expire_seconds = 2592000
        self.scene_id = GetRandomStr().digits_(4)
        self.scene_str = GetRandomStr().lowercase_(4)
        self.temporaryQRCode_url = 'https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token={0}'.format(
            self.access_token)
        self.permanentQRCode_url = 'https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token={0}'.format(
            self.access_token)
        self.getQRCode_url = 'https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket={0}'

    def temporary_QRCode_int(self):
        """
        临时二维码
        :return:
        """
        params_json = {
            "expire_seconds": self.expire_seconds,
            "action_name": "QR_SCENE",
            "action_info": {
                "scene": {
                    "scene_id": self.scene_id
                }
            }
        }
        ret_temporary_QRCode_int = requests.post(self.temporaryQRCode_url, json=params_json)
        ret_temporary_QRCode_int = json.loads(ret_temporary_QRCode_int.text)

        ticket = ret_temporary_QRCode_int['ticket']
        expire_seconds = ret_temporary_QRCode_int['expire_seconds']
        url = ret_temporary_QRCode_int['url']

        ret_getQRCode = requests.get(self.getQRCode_url.format(ticket))
        try:
            with open(
                    os.path.join(os.getcwd(), r'wechat\AccountManage\png\{}_temporary_int.png'.format(self.scene_str)),
                    "wb") as f:
                f.write(ret_getQRCode.content)
            return True
        except:
            raise

    def temporary_QRCode_str(self):
        """
        临时二维码
        :return:
        """
        params_json = {
            "expire_seconds": self.expire_seconds,
            "action_name": "QR_STR_SCENE",
            "action_info": {
                "scene": {
                    "scene_str": self.scene_str
                }
            }
        }
        ret_temporary_QRCode_str = requests.post(self.temporaryQRCode_url, json=params_json)
        ret_temporary_QRCode_str = json.loads(ret_temporary_QRCode_str.text)

        ticket = ret_temporary_QRCode_str['ticket']
        expire_seconds = ret_temporary_QRCode_str['expire_seconds']
        url = ret_temporary_QRCode_str['url']

        ret_getQRCode = requests.get(self.getQRCode_url.format(ticket))
        try:
            with open(
                    os.path.join(os.getcwd(), r'wechat\AccountManage\png\{}_temporary_str.png'.format(self.scene_str)),
                    "wb") as f:
                f.write(ret_getQRCode.content)
            return True
        except:
            raise

    def permanent_QRcode_int(self):
        """
        永久二维码
        :return:
        """
        params_json = {
            "action_name": "QR_LIMIT_SCENE",
            "action_info": {
                "scene": {
                    "scene_id": self.scene_id
                }
            }
        }
        ret_permanent_QRcode_int = requests.post(self.temporaryQRCode_url, json=params_json)
        ret_permanent_QRcode_int = json.loads(ret_permanent_QRcode_int.text)

        ticket = ret_permanent_QRcode_int['ticket']
        url = ret_permanent_QRcode_int['url']

        ret_getQRCode = requests.get(self.getQRCode_url.format(ticket))
        try:
            with open(
                    os.path.join(os.getcwd(), r'wechat\AccountManage\png\{}_permanent_int.png'.format(self.scene_str)),
                    "wb") as f:
                f.write(ret_getQRCode.content)
            return True
        except:
            raise

    def permanent_QRcode_str(self):
        """
        永久二维码
        :return:
        """
        params_json = {
            "action_name": "QR_LIMIT_STR_SCENE",
            "action_info": {
                "scene": {
                    "scene_str": self.scene_str
                }
            }
        }
        ret_permanent_QRcode_str = requests.post(self.temporaryQRCode_url, json=params_json)
        ret_permanent_QRcode_str = json.loads(ret_permanent_QRcode_str.text)

        ticket = ret_permanent_QRcode_str['ticket']
        url = ret_permanent_QRcode_str['url']

        ret_getQRCode = requests.get(self.getQRCode_url.format(ticket))
        try:
            with open(
                    os.path.join(os.getcwd(), r'wechat\AccountManage\png\{}_permanent_str.png'.format(self.scene_str)),
                    "wb") as f:
                f.write(ret_getQRCode.content)
            return True
        except:
            raise

