ACCESS_TOKEN_EXPIRED = 15 * 60

# 自定义菜单模板
menu_params01 = {
    "button": [
        {
            "type": "click",
            "name": "今日歌曲",
            "key": "V1001_TODAY_MUSIC"
        },
        {
            "name": "菜单",
            "sub_button": [
                {
                    "type": "view",
                    "name": "搜索",
                    "url": "http://www.soso.com/"  # EventKey
                },
                # {
                #     "type": "miniprogram",
                #     "name": "wxa",
                #     "url": "http://mp.weixin.qq.com",
                #     "appid": "wx286b93c14bbf93aa",
                #     "pagepath": "pages/lunar/index"
                # },
                {
                    "type": "click",
                    "name": "赞一下我们",
                    "key": "V1001_GOOD"
                }]
        }]
}

# 设置所属行业
industry_params01 = {
    "industry_id1": "1",
    "industry_id2": "2"
}

# 设置模板库中模板的编号
template_id_short_params01 = {
    "template_id_short": "TM00001"
}

# 设置模板ID
template_id_params01 = {
    # 购买成功通知
    "template_id": "p0TuxswF4Lo-jhVSDV8g-QLNgXdfm_St9dVXMlsutDo"
}

# 设置的模板内容
set_content_of_template = {
    "content": "购买成功通知"
               "{{first.DATA}}\
                \
               商品信息：{{keyword1.DATA}}\
               商品价格：{{keyword2.DATA}}\
               {{remark.DATA}}"
}

# 发送模板消息
send_template_msg_params01 = {
    "touser": "oLiV45mMC03ifHcPWa8C32qDq_oQ",
    "template_id": "p0TuxswF4Lo-jhVSDV8g-QLNgXdfm_St9dVXMlsutDo",
    # "url": "http://weixin.qq.com/download",
    # "miniprogram": {
    #     "appid": "xiaochengxuappid12345",
    #     "pagepath": "index?foo=bar"
    # },
    "data": {
        "first": {
            "value": "您好，您已经购买成功!",
            "color": "#173177"
        },
        "keyword1": {
            "value": "巧克力",
            "color": "#173177"
        },
        "keyword2": {
            "value": "39.8元",
            "color": "#173177"
        },
        "remark": {
            "value": "欢迎再次购买！",
            "color": "#173177"
        }
    }
}

