import json
import requests

from dtwechat.settings import APP_ID, APP_SECRET
from wechat.Start.startDev import get_access_token


def setcomment(openid_lst, comment_lst):
    access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')
    url_set = 'https://api.weixin.qq.com/cgi-bin/user/info/updateremark?access_token={0}'.format(access_token)

    if len(openid_lst) == len(comment_lst):
        for i in range(len(openid_lst)):
            params = {
                "openid": openid_lst[i],
                "remark": comment_lst[i]
            }
            ret_setcomment = requests.post(url_set,
                                           json.dumps(params, ensure_ascii=False).encode('utf-8'))
            ret_setcomment = json.loads(ret_setcomment.text)
            print(ret_setcomment)
    else:
        print('函数传参不正确')

