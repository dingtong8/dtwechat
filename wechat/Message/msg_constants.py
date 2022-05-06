params_upload_text_msg = {
    "articles": [
        {
            "thumb_media_id": "kk_W_apeBeUiuNwPQ73qO2m5XbfyAZ1SxLJMgFD6xSkitTMxlY3bb0xLuZlsn6n-",
            "author": "dingtong",
            "title": "Happy Day",
            "content_source_url": "http://mmbiz.qpic.cn/mmbiz_jpg/lHKnIHDBWDtK5Mia2mcWL3j1zp64b8feXqFd1lBwlDEzsaS2zGwW5Jsl4hWUfUXdVH6GYWyUY7C4FccqvzLScmg/0",
            "content": "content",
            "digest": "digest",
            "show_cover_pic": 1,
            "need_open_comment": 1,
            "only_fans_can_comment": 1
        },
        {
            "thumb_media_id": "kk_W_apeBeUiuNwPQ73qO2m5XbfyAZ1SxLJMgFD6xSkitTMxlY3bb0xLuZlsn6n-",
            "author": "dingtong",
            "title": "Happy Day",
            "content_source_url": "http://mmbiz.qpic.cn/mmbiz_jpg/lHKnIHDBWDtK5Mia2mcWL3j1zp64b8feXqFd1lBwlDEzsaS2zGwW5Jsl4hWUfUXdVH6GYWyUY7C4FccqvzLScmg/0",
            "content": "content",
            "digest": "digest",
            "show_cover_pic": 0,
            "need_open_comment": 1,
            "only_fans_can_comment": 1
        }
    ]
}

# 上传视频
params_upload_video = {

}

# 图文消息模板
params_img_text = {
    "filter": {
        "is_to_all": False,
        "tag_id": 2
    },
    "mpnews": {
        "media_id": "{0}"
    },
    "msgtype": "mpnews",
    "send_ignore_reprint": 0,
    "clientmsgid": "send_tag_2"
}

# 文本消息模板
params_text = {
    "filter": {
        "is_to_all": False,
        "tag_id": 2
    },
    "text": {
        "content": "{0}"
    },
    "msgtype": "text",
    "clientmsgid": "send_tag_2"
}

# 音频消息
params_voice = {
    "filter": {
        "is_to_all": False,
        "tag_id": 2
    },
    "voice": {
        "media_id": "{0}"
    },
    "msgtype": "voice",
    "clientmsgid": "send_tag_2"
}

# 图片消息
params_img = {
    "filter": {
        "is_to_all": False,
        "tag_id": 2
    },
    "images": {
        "media_ids": "{0}",
        "recommend": "{1}",
        "need_open_comment": 1,
        "only_fans_can_comment": 0
    },
    "msgtype": "image",
    "clientmsgid": "send_tag_2"
}

# 视频消息
params_video = {
    "media_id": "{0}",
    "title": "{1}",
    "description": "{2}",
    "clientmsgid": "send_tag_2"
}
