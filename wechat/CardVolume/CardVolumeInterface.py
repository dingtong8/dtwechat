import json

import requests

from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Start.startDev import get_access_token


class CardVolume:
    """
    卡券HelloWorld
    """

    def __init__(self):
        self.access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')

    def create_card_volume(self, imgpath):
        """
        创建卡卷
        :return:
        """
        url_1 = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token={0}'.format(self.access_token)

        with open(imgpath, 'rb') as f:
            fileStream = f.read()

        params_1 = {
            "buffer": fileStream
        }

        ret_url_1 = requests.post(url_1, files=params_1)
        ret_url_1 = json.loads(ret_url_1.text)
        print(ret_url_1)

        url_2 = 'https://api.weixin.qq.com/card/create?access_token={0}'.format(self.access_token)
        params_2 = {
            "card": {
                "card_type": "GROUPON",
                "groupon": {
                    "base_info": {
                        "logo_url":
                            "http://mmbiz.qpic.cn/mmbiz/iaL1LJM1mF9aRKPZJkmG8xXhiaHqkKSVMMWeN3hLut7X7hicFNjakmxibMLGWpXrEXB33367o7zHN0CwngnQY7zb7g/0",
                        "brand_name": "微信餐厅",
                        "code_type": "CODE_TYPE_TEXT",
                        "title": "132元双人火锅套餐",
                        "color": "Color010",
                        "notice": "使用时向服务员出示此券",
                        "service_phone": "020-88888888",
                        "description": "不可与其他优惠同享\n如需团购券发票，请在消费时向商户提出\n店内均可使用，仅限堂食",
                        "date_info": {
                            "type": "DATE_TYPE_FIX_TIME_RANGE",
                            "begin_timestamp": 1397577600,
                            "end_timestamp": 1472724261
                        },
                        "sku": {
                            "quantity": 500000
                        },
                        "use_limit": 100,
                        "get_limit": 3,
                        "use_custom_code": False,
                        "bind_openid": False,
                        "can_share": True,
                        "can_give_friend": True,
                        "location_id_list": [
                            123,
                            12321,
                            345345
                        ],
                        "center_title": "顶部居中按钮",
                        "center_sub_title": "按钮下方的wording",
                        "center_url": "www.qq.com",
                        "custom_url_name": "立即使用",
                        "custom_url": "",
                        "custom_url_sub_title": "6个汉字tips",
                        "promotion_url_name": "更多优惠",
                        "promotion_url": "",
                        "source": "大众点评"
                    },
                    "advanced_info": {
                        "use_condition": {
                            "accept_category": "鞋类",
                            "reject_category": "阿迪达斯",
                            "can_use_with_other_discount": True
                        },
                        "abstract": {
                            "abstract": "微信餐厅推出多种新季菜品，期待您的光临",
                            "icon_url_list": [
                                "http://mmbiz.qpic.cn/mmbiz/p98FjXy8LacgHxp3sJ3vn97bGLz0ib0Sfz1bjiaoOYA027iasqSG0sjpiby4vce3AtaPu6cIhBHkt6IjlkY9YnDsfw/0"
                            ]
                        },
                        "text_image_list": [
                            {
                                "image_url": "http://mmbiz.qpic.cn/mmbiz/p98FjXy8LacgHxp3sJ3vn97bGLz0ib0Sfz1bjiaoOYA027iasqSG0sjpiby4vce3AtaPu6cIhBHkt6IjlkY9YnDsfw/0",
                                "text": "此菜品精选食材，以独特的烹饪方法，最大程度地刺激食 客的味蕾"
                            },
                            {
                                "image_url": "http://mmbiz.qpic.cn/mmbiz/p98FjXy8LacgHxp3sJ3vn97bGLz0ib0Sfz1bjiaoOYA027iasqSG0sjpiby4vce3AtaPu6cIhBHkt6IjlkY9YnDsfw/0",
                                "text": "此菜品迎合大众口味，老少皆宜，营养均衡"
                            }
                        ],
                        "time_limit": [
                            {
                                "type": "MONDAY",
                                "begin_hour": 0,
                                "end_hour": 10,
                                "begin_minute": 10,
                                "end_minute": 59
                            },
                            {
                                "type": "HOLIDAY"
                            }
                        ],
                        "business_service": [
                            "BIZ_SERVICE_FREE_WIFI",
                            "BIZ_SERVICE_WITH_PET",
                            "BIZ_SERVICE_FREE_PARK",
                            "BIZ_SERVICE_DELIVER"
                        ]
                    },
                    "deal_detail": "以下锅底2选1（有菌王锅、麻辣锅、大骨锅、番茄锅、清补 凉锅、酸菜鱼锅可选）：\n大锅1份 12元\n小锅2份 16元 "
                }
            }}

        ret_url_2 = requests.post(url_2, json=params_2)
        ret_url_2 = json.loads(ret_url_2.text)
        print(ret_url_2)

    def statistics_card_volume(self):
        url = 'https://api.weixin.qq.com/datacube/getcardbizuininfo?access_token={0}'.format(self.access_token)

        params = {
            "begin_date": "2021-06-15",
            "cond_source": 0
        }

        ret_url = requests.post(url, params)
        ret_url = json.loads(ret_url.text)
        print(ret_url)


