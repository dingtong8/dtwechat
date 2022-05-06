import json

import requests

from wechat.Start.startDev import get_access_token
from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Message.msg_constants import params_img_text, params_text, params_voice, params_img, \
    params_video, params_upload_text_msg, params_upload_video


class MassMsg:
    """
    群发消息
    https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Batch_Sends_and_Originality_Checks.html#0
    """

    def __init__(self, imgpath):
        self.params_upload_text_msg = params_upload_text_msg
        self.imgpath = imgpath
        self.params_img_text = params_img_text
        self.params_text = params_text
        self.params_voice = params_voice
        self.params_img = params_img
        self.params_video = params_video
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')

    def upload_img(self):
        """
        上传图文消息内的图片获取URL
        :return: 图片 URL
        """
        url_upload_img = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token={0}'.format(self.access_token)

        params = {'media': open('{}'.format(self.imgpath), 'rb')}
        ret_url_upload = requests.post(url_upload_img, files=params)
        ret_url_upload = json.loads(ret_url_upload.content.decode())
        print(ret_url_upload)

        return ret_url_upload

    def upload_text_msg(self):
        """
        上传图文消息素材
        :return:
        """
        url_upload_text_msg = 'https://api.weixin.qq.com/cgi-bin/media/uploadnews?access_token={0}'.format(
            self.access_token)

        params = params_upload_text_msg

        ret_url_upload_text_msg = requests.post(url_upload_text_msg,
                                                json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_url_upload_text_msg = json.loads(ret_url_upload_text_msg.text)
        print(ret_url_upload_text_msg)

        return ret_url_upload_text_msg

    def upload_video(self):
        url_upload_video = 'https://api.weixin.qq.com/cgi-bin/media/uploadvideo?access_token={0}'.format(
            self.access_token)

        params = params_upload_video

        ret_url_upload_video = requests.post(url_upload_video,
                                             json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_url_upload_video = json.loads(ret_url_upload_video.text)
        print(ret_url_upload_video)

        return ret_url_upload_video

    def label_mass_msg(self, img_text=None, text=None, voice=None, img=None, video=None):
        """
        根据标签进行群发
        :return:
        """
        url_label_mass_msg = 'https://api.weixin.qq.com/cgi-bin/message/mass/sendall?access_token={0}'.format(
            self.access_token)

        if img_text:
            # ret_text_msg = self.upload_text_msg()
            ret_text_msg = {'type': 'news',
                            'media_id': 'zYynNVGEVbfc6pWWWxTUcwjdISLrZNAMoGzNbgETHFmyOChtU8xYX8LF86RQoZMd',
                            'created_at': 1625132634, 'item': []}
            media_id = ret_text_msg['media_id']

            params_img_text['mpnews']['media_id'] = media_id
            params = params_img_text
            print(params)

            ret_mass_img_text = requests.post(url_label_mass_msg,
                                              json.dumps(params, ensure_ascii=False).encode('utf-8'))
            ret_mass_img_text = json.loads(ret_mass_img_text.text)
            print(ret_mass_img_text)

        elif text:
            params_text['text']['content'] = text
            params = params_text
            print(params)

            ret_mass_text = requests.post(url_label_mass_msg,
                                          json.dumps(params, ensure_ascii=False).encode('utf-8'))
            ret_mass_img_text = json.loads(ret_mass_text.text)
            print(ret_mass_img_text)

        elif voice:
            # ret_voice_msg = self.upload_text_msg()
            ret_voice_msg = {'type': 'voice',
                             'media_id': 'iBgNjmHaWUZJujCFgPv2HgVr5Z57FsGgPHt4gvNStNC44WqZq-IW3alf_VN1vj4I',
                             'created_at': 1625189207, 'item': []}
            params_voice['voice']['media_id'] = ret_voice_msg['media_id']
            params = params_voice
            print(params)

            ret_mass_voice = requests.post(url_label_mass_msg,
                                           json.dumps(params, ensure_ascii=False).encode('utf-8'))
            ret_mass_voice = json.loads(ret_mass_voice.text)
            print(ret_mass_voice)

        elif img:
            # ret_text_msg_msg = self.upload_text_msg()
            ret_img_msg = {'type': 'news',
                           'media_id': 'pCmkJWntxvwmxqcvML6rSKG6hg_BUErcvlkAR3wWVIMsGwIqNvTjEYbqzkxiU9mY',
                           'created_at': 1625190022, 'item': []}
            params_img['images']['media_ids'] = ret_img_msg['media_id']
            params_img['images']['recommend'] = ''
            params = params_img
            print(params)

            ret_mass_img = requests.post(url_label_mass_msg,
                                         json.dumps(params, ensure_ascii=False).encode('utf-8'))
            ret_mass_img = json.loads(ret_mass_img.text)
            print(ret_mass_img)

        elif video:
            # ret_video_msg = self.upload_video()
            url_video_mass_msg = 'https://api.weixin.qq.com/cgi-bin/media/uploadvideo?access_token={0}'.format(
                self.access_token)

            ret_video_msg = {'type': 'mpvideo',
                             'media_id': 'vHMrqY2IF8sd8srJ3nmOMXjF4NaBXFnIv8wlr5s4e5UcZX344g8VmlhGFUi2H5fG',
                             'created_at': 1625190478, 'item': []}
            params_video['media_id'] = ret_video_msg['media_id']
            params_video['title'] = ret_video_msg['media_id']
            params_video['description'] = ret_video_msg['media_id']
            params = params_video
            print(params)

            ret_mass_video = requests.post(url_video_mass_msg,
                                           json.dumps(params, ensure_ascii=False).encode('utf-8'))
            ret_mass_video = json.loads(ret_mass_video.text)
            print(ret_mass_video)

    def openid_mass_msg(self, img_text=None, text=None, voice=None, img=None, video=None, ):
        pass

    def delete_mass_msg(self, msg_id, article_idx):
        """
        删除群发
        :return:
        """
        url_del_mass_msg = 'https://api.weixin.qq.com/cgi-bin/message/mass/delete?access_token={}'.format(
            self.access_token)

        params = {
            "msg_id": msg_id,
            "article_idx": article_idx
        }

        ret_del_mass_msg = requests.post(url_del_mass_msg,
                                         json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_del_mass_msg = json.loads(ret_del_mass_msg.text)
        print(ret_del_mass_msg)

    def preview_mass_msg(self, OPENID, media_id, msgtype, img_text=None, text=None, voice=None, img=None, video=None):
        url_preview_mass_msg = 'https://api.weixin.qq.com/cgi-bin/message/mass/preview?access_token={0}'.format(
            self.access_token)

        params = {
            "touser": OPENID,
            "mpnews": {
                "media_id": media_id
            },
            "msgtype": msgtype
        }

        if img_text:
            pass

        if text:
            pass

        if voice:
            pass

        if img:
            pass

        if video:
            pass

    def query_mass_status(self, msg_id):
        ret_query_mass_status = 'https://api.weixin.qq.com/cgi-bin/message/mass/get?access_token={0}'.format(
            self.access_token)

        params = {
            "msg_id": msg_id
        }

        ret_query_mass_status = requests.post(ret_query_mass_status,
                                              json.dumps(params, ensure_ascii=False).encode('utf-8'))
        ret_query_mass_status = json.loads(ret_query_mass_status.text)
        print(ret_query_mass_status)

    def limit_mass_speed(self, speed):
        """控制群发速度"""
        url_limit_mass_speed = 'https://api.weixin.qq.com/cgi-bin/message/mass/speed/get?access_token={}'.format(
            self.access_token)
        ret_limit_mass_speed = requests.post(url_limit_mass_speed)
        ret_limit_mass_speed = json.loads(ret_limit_mass_speed.text)
        print(ret_limit_mass_speed)

        params = {
            "speed": int(speed)
        }

        url_set_mass_speed = 'https://api.weixin.qq.com/cgi-bin/message/mass/speed/set?access_token={}'.format(self.access_token)
        ret_set_mass_speed = requests.post(url_set_mass_speed, params=params)
        ret_set_mass_speed = json.loads(ret_set_mass_speed.text)
        print(ret_set_mass_speed)

    def get_autoreply_rule(self):
        url_get_autoreply_rule = 'https://api.weixin.qq.com/cgi-bin/get_current_autoreply_info?access_token={0}'.format(self.access_token)

        ret_get_autoreply_rule = requests.get(url_get_autoreply_rule)
        ret_get_autoreply_rule = json.loads(ret_get_autoreply_rule.text)
        print(ret_get_autoreply_rule)

    def get_category(self):
        """获取公众号类目"""
        url_get_category = 'https://api.weixin.qq.com/wxaapi/newtmpl/getcategory?access_token={0}'.format(self.access_token)

        ret_get_category = requests.get(url_get_category)
        ret_get_category = json.loads(ret_get_category.text)
        print(ret_get_category)

    def get_template_key_words(self):
        """获取模板中的关键词"""
        url_get_template_key_words = 'https://api.weixin.qq.com/wxaapi/newtmpl/getpubtemplatekeywords?access_token={0}'.format(self.access_token)

        ret_get_template_key_words = requests.get(url_get_template_key_words)
        ret_get_template_key_words = json.loads(ret_get_template_key_words.text)
        print(ret_get_template_key_words)


