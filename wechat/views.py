import datetime
import hashlib
import json
import time
import uuid

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from wechat.AccountManage.GenerateParameterQRCode import CreateQRcode
from wechat.Invoice.non_tax_paper import WechatInvoice
from wechat.Message import receive, reply
from dtwechat.settings import TOKEN, APP_ID, APP_SECRET
from wechat.Message.massMsg import MassMsg
from wechat.Start.startDev import get_access_token
from wechat.models import Wechat
from wechat.tools import GetRandomStr


@csrf_exempt
def weixin_main(request):
    # 接收微信服务器get请求发过来的参数
    if request.method == "GET":
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)

        # 服务器配置中的token
        token = TOKEN
        # 把参数放到list中排序后合成一个字符串，再用sha1加密得到新的字符串与微信发来的signature对比，如果相同就返回echostr给服务器，校验通过
        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        hashstr = ''.join([s for s in hashlist])
        hashstr = hashlib.sha1(hashstr.encode("utf-8")).hexdigest()
        if hashstr == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("field")
    else:
        # request.method == "POST":
        # 开发者发送的消息(xml 格式)
        othercontent = autoreply(request)
        print(othercontent)
        return HttpResponse(othercontent)


def autoreply(request):
    """
    # POST 请求
    参考：https://developers.weixin.qq.com/doc/offiaccount/Getting_Started/Getting_Started_Guide.html
    :param request:
    # 消息
    text
    image
    voice
    video
    shortvideo
    location
    link
    music
    # 事件
    CLICK
    VIEW
    subscribe
    unsubscribe
    :return:
    """
    try:
        # webData 粉丝发送的消息
        webData = request.body
        print('webData: ', webData)
        recMsg = receive.parse_xml(webData)
        # print("recMsg", recMsg)
        # print(isinstance(recMsg, receive.EventMsg))

        # 接收普通消息
        if isinstance(recMsg, receive.Msg):
            FromUserName = recMsg.ToUserName
            ToUserName = recMsg.FromUserName
            if recMsg.MsgType == 'text':
                content = "您好,欢迎来到Python大学习!希望我们可以一起进步!"
                MsgId = recMsg.MsgId
                replyMsg = reply.TextMsg(ToUserName, FromUserName, content, MsgId)
                # time.sleep(10) # 微信后台发起了三次重试操作
                return replyMsg.send()
            elif recMsg.MsgType == 'image':
                PicUrl = recMsg.PicUrl
                MediaId = recMsg.MediaId
                MsgId = recMsg.MsgId
                replyMsg = reply.ImageMsg(ToUserName, FromUserName, MediaId, PicUrl, MsgId)
                return replyMsg.send()
            elif recMsg.MsgType == 'voice':
                mediaId = recMsg.MediaId
                Format = recMsg.Format
                MsgId = recMsg.MsgId
                Recognition = recMsg.Recognition
                replyMsg = reply.VoiceMsg(ToUserName, FromUserName, mediaId, Format, MsgId, Recognition)
                return replyMsg.send()
            elif recMsg.MsgType == 'video':
                MsgId = recMsg.MsgId
                MediaId = recMsg.MediaId
                ThumbMediaId = recMsg.ThumbMediaId
                replyMsg = reply.VideoMsg(ToUserName, FromUserName, MediaId, ThumbMediaId, MsgId)
                return replyMsg.send()
            elif recMsg.MsgType == 'shortvideo':
                mediaId = recMsg.MediaId
                ThumbMediaId = recMsg.ThumbMediaId
                replyMsg = reply.ShortVideoMsg(ToUserName, FromUserName, ThumbMediaId)
                return replyMsg.send()
            elif recMsg.MsgType == 'location':
                Location_X = recMsg.Location_X
                Location_Y = recMsg.Location_Y
                Scale = recMsg.Scale
                Label = recMsg.Label
                MsgId = recMsg.MsgId
                MsgType = recMsg.MsgType
                replyMsg = reply.LocationMsg(ToUserName, FromUserName, Location_X, Location_Y, Scale, Label, MsgId,
                                             MsgType)
                return replyMsg.send()
            elif recMsg.MsgType == 'link':
                Title = recMsg.Title
                MsgType = recMsg.MsgType
                Description = recMsg.Description
                Url = recMsg.Url
                MsgId = recMsg.MsgId
                replyMsg = reply.LinkMsg(ToUserName, FromUserName, Title, Description, Url, MsgId, MsgType)
                return replyMsg.send()
            elif recMsg.MsgType == 'music':
                mediaId = recMsg.MediaId
                Title = recMsg.Title
                Description = recMsg.Description
                MsgType = recMsg.MsgType
                MusicUrl = recMsg.MusicUrl
                HQMusicUrl = recMsg.HQMusicUrl
                ThumbMediaId = recMsg.ThumbMediaId
                replyMsg = reply.MusicMsg(ToUserName, FromUserName, mediaId, MsgType, Title, Description, MusicUrl,
                                          HQMusicUrl, ThumbMediaId)
                return replyMsg.send()
        # 接收事件推送
        elif isinstance(recMsg, receive.EventMsg):
            FromUserName = recMsg.ToUserName
            ToUserName = recMsg.FromUserName
            MsgId = 'MsgId'
            if recMsg.MsgType == 'event':
                if recMsg.Event == 'CLICK':
                    if recMsg.EventKey == 'V1001_TODAY_MUSIC':
                        # content = "编写中，尚未完成"
                        # replyMsg = reply.TextMsg(ToUserName, FromUserName, content, MsgId)
                        MsgType = recMsg.MsgType
                        Event = recMsg.Event
                        EventKey = recMsg.EventKey
                        replyMsg = reply.ClickMsg(ToUserName, FromUserName, MsgType, Event, EventKey)
                        return replyMsg.send()
                elif recMsg.Event == 'VIEW':
                    if recMsg.EventKey == 'http://www.soso.com/':
                        MsgType = recMsg.MsgType
                        Event = recMsg.Event
                        EventKey = recMsg.EventKey
                        MenuId = recMsg.MenuId
                        replyMsg = reply.ViewMsg(ToUserName, FromUserName, MsgType, Event, EventKey, MenuId)
                        return replyMsg.send()
                elif recMsg.Event == 'LOCATION':
                    Latitude = recMsg.Latitude
                    Longitude = recMsg.Longitude
                    Precision = recMsg.Precision
                    MsgType = recMsg.MsgType
                    Event = recMsg.Event
                    replyMsg = reply.LOCATIONMSG(ToUserName, FromUserName, MsgType, Event, Latitude, Longitude, Precision)
                    return replyMsg.send()
                elif recMsg.Event == 'subscribe':
                    content = "你好，欢迎关注🎈🎆🎇✨"
                    replyMsg = reply.TextMsg(ToUserName, FromUserName, content, MsgId)
                    query_fan = Wechat.objects.filter(FromUserName=ToUserName)
                    if query_fan:
                        # 旧用户
                        Wechat.objects.filter(FromUserName=ToUserName).update(state=0,
                                                                              CreateTime=datetime.datetime.now())
                    else:
                        # 新用户
                        fans = Wechat(FromUserName=ToUserName, ToUserName=FromUserName, state=0)
                        fans.save()
                    return replyMsg.send()
                elif recMsg.Event == 'unsubscribe':
                    MsgType = recMsg.MsgType
                    Event = recMsg.Event
                    EventKey = recMsg.EventKey
                    replyMsg = reply.SubscribeMsg(ToUserName, FromUserName, MsgType, Event, EventKey)
                    Wechat.objects.filter(FromUserName=ToUserName).update(state=1, CreateTime=datetime.datetime.now())
                    return replyMsg.send()
                else:
                    print("暂且不处理")
                    return reply.Msg().send()
        else:
            print("暂且不处理")
            return reply.Msg().send()
    except Exception as e:
        print('e', e)
        return e


def index(request):
    return render(request, "index.html")


@csrf_exempt
def get_signature(request):
    """
    生成签名算法
    返回微信 config 接口注入权限验证配置参数
    :param request:
    :return:
    """
    ret_get_signature = {}

    if request.method == "GET":
        siteUrl = request.GET.get('siteUrl', 'http://127.0.0.1:8080/wx/get_signature/')
        jsapi_ticket = WechatInvoice().get_ticket()['ticket']
        nonceStr = GetRandomStr().lower_uppercase_digits(16)
        timestamp = int(time.time())

        string = {
            'nonceStr': nonceStr,
            'timestamp': timestamp,
            'jsapi_ticket': jsapi_ticket,
            'url': siteUrl
        }

        # string1 = "jsapi_ticket={}&nonceStr={}&timestamp={}&url={}".format(jsapi_ticket, nonceStr, timestamp, siteUrl)
        string = '&'.join(['%s=%s' % (key.lower(), string[key]) for key in sorted(string)]).encode('utf-8')
        signature = hashlib.sha1(string).hexdigest()

        ret_get_signature = {
            "nonceStr": nonceStr,
            "timestamp": timestamp,
            "signature": signature,
            "appId": APP_ID,
            "url": siteUrl
        }
        # ret_get_signature = json.dumps(ret_get_signature, ensure_ascii=False)
    print(ret_get_signature)
    return render(request, "cfg_jurisdiction.html", {"ret_get_signature": ret_get_signature})
    # return JsonResponse(ret_get_signature)


# from wechat.Start.startDev import get_access_token
# from dtwechat.settings import APP_ID, APP_SECRET
# get_access_token(APP_ID, APP_SECRET)
# from wechat.Webdev.webAuthorization import WEBAuthorization
# WEBAuthorization().pull_user_info('46_jMtzdVO_qe7u3iHwW07gAgX-dyledXkrlOdez1FFQfr-5flvIKxrdNtO0uFgMIh2tGgUYjtnrDcoxKEFspvO0RcPL4uIDzS3KoDtdMLpg6E', 'oLiV45hlll9pxr3PG13DZxjtZHvc')
# from wechat.Invoice.non_tax_paper import WechatInvoice
# WechatInvoice().get_ticket()
# from wechat.UserManage.getUserInfo import GetInfo
# filelength = r'D:\Code\dtwechat\wechat\Message\png\91303d33c6812bf38226107c915f1cf.jpg'
# filetype = 'image'
# MaterialCorrelation().add_temporary(filelength, filetype)
# LabelManage().batch_unset_fan_label(['oLiV45hlll9pxr3PG13DZxjtZHvc'], '武汉')
# LabelManage().get_fan_labels(['oLiV45hlll9pxr3PG13DZxjtZHvc'])
# MaterialCorrelation().get_temporary('xy7XZonHot64JEOUD9882IPJoHZgCfFJmzHQQf2v_QaaTGmfwhT0jtj9o-CTZDML', filetype)
# MassMsg(filelength).upload_img()
# setcomment(['oLiV45hlll9pxr3PG13DZxjtZHvc'], ['丁童'])
# GetInfo().batch_get_userinfo(['oLiV45hlll9pxr3PG13DZxjtZHvc', 'oLiV45mMC03ifHcPWa8C32qDq_oQ'])
# from wechat.UserManage.getUserList import UserManage
# UserManage().get_user_lst()
# from wechat.UserManage.blacklistManage import BlackListManage
# BlackListManage().get_black_lst()
# CreateQRcode().permanent_QRcode_str()
# from wechat.DataStatistics.InterfaceAnalysis import InternetSnalysis
# InternetSnalysis().getinterfacesummary('2021-07-09', '2021-07-09')
# from wechat.WeChatStores.StoreRelated import StoreRelated
# imgpath = r'D:\Code\dtwechat\wechat\Message\png\2026538069305462784-1.JPG'
# StoreRelated().get_province()
# from wechat.Intelligent.SemanticComprehension import SemanticComprehensionPrs
# SemanticComprehensionPrs().comprehension('oLiV45hlll9pxr3PG13DZxjtZHvc')



