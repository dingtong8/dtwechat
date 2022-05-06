import json
import time
import requests


from django_redis import get_redis_connection
from wechat.Menu.menu_constants import ACCESS_TOKEN_EXPIRED
from dtwechat.settings import APP_ID, APP_SECRET


def fresh_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh'):
    """
    从微信接口刷新(获取) access_token
    将获取的 access_token 存入 redis 数据库
    :param APP_ID:
    :param APP_SECRET:
    :param access_token_type:
    :return: 新的 access_token
    """
    access_token = ''
    access_token_key = ''
    req_url = 'https://api.weixin.qq.com/cgi-bin/token'
    # https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET
    params = {
        'grant_type': 'client_credential',
        'appid': APP_ID,
        'secret': APP_SECRET
    }

    if access_token_type == 'test_gzh':
        access_token_key = 'wx_gzh_access_token'
    elif access_token_type == 'test_xcx':
        pass

    try:
        if access_token_type == 'test_gzh':
            req = requests.get(req_url, params=params, timeout=3)
            json_data = json.loads(req.text)
            access_token = json_data.get('access_token')
            # 连接 redis
            redis_conn = get_redis_connection("access_token")
            # redis 设置值
            redis_conn.setex(access_token_key, ACCESS_TOKEN_EXPIRED, access_token)
        elif access_token_type == 'test_xcx':
            pass
    except Exception as e:
        msg_error = "向第三方服务端发送请求获取access_token失败：{0}".format(e)
        raise ConnectionError(msg_error)

    return access_token


def get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh'):
    """
    从 redis 上获取 access_token
    """
    access_token_key = ''
    if access_token_type == 'test_gzh':
        access_token_key = 'wx_gzh_access_token'
    elif access_token_type == 'test_xcx':
        pass

    redis_conn = get_redis_connection("access_token")
    access_token = redis_conn.get(access_token_key)
    if access_token and access_token != 'None':
        access_token = access_token.decode()
        print('redis access_token', access_token)
    else:
        print('redis 中没有记录 access_token, 即将重新获取')

    # 如果从redis获取缓存失败，则从微信api获取并存储在redis里面
    if not access_token or access_token == 'None':
        access_token = fresh_access_token(APP_ID, APP_SECRET, access_token_type)

    return access_token


def get_wx_service_ip():
    """
    获取微信API接口 IP地址
    获取微信callback IP地址
    :return: api_ip_list callback_ip_list
    """
    access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')
    url_api_ip = 'https://api.weixin.qq.com/cgi-bin/get_api_domain_ip?access_token={0}'.format(access_token)
    url_callback_ip = 'https://api.weixin.qq.com/cgi-bin/getcallbackip?access_token={0}'.format(access_token)

    ret_api_ip = requests.get(url_api_ip, timeout=3)
    api_ip_list = ret_api_ip.text

    ret_callback_ip = requests.get(url_callback_ip, timeout=3)
    callback_ip_list = ret_callback_ip.text

    return api_ip_list, callback_ip_list


def ping_wx_service_ip():
    """
    为了帮助开发者排查回调连接失败的问题，提供这个网络检测的API。
    它可以对开发者URL做域名解析，然后对所有IP进行一次ping操作，得到丢包率和耗时。
    :return: 返回检测结果
    """
    access_token = get_access_token(APP_ID, APP_SECRET, access_token_type='test_gzh')
    url_network_detection = 'https://api.weixin.qq.com/cgi-bin/callback/check?access_token={0}'.format(access_token)

    params = {
        "action": "all",
        "check_operator": "DEFAULT"
    }

    while True:
        try:
            network_check = requests.post(url_network_detection, json=params, timeout=3)
            ret_network_check = json.loads(network_check.text)
            print(ret_network_check)
            print(ret_network_check.get('ping'))
            if ret_network_check.get('ping')[0]['package_loss'] != '0%':
                print('开发者URL做域名解析，然后对所有IP进行一次ping操作丢包：{0}'.format(ret_network_check))
            else:
                print('ping_wx_service_ip ok')
            break
        except TypeError:
            print(TypeError)
            time.sleep(10)

    return ret_network_check


