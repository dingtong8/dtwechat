# description: 回复消息


import time


class Msg(object):
    def __init__(self):
        pass

    def send(self):
        return "success"


class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content, MsgId):
        super().__init__()
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content
        self.__dict['MsgId'] = MsgId

    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[{Content}]]></Content>
                <MsgId><![CDATA[{MsgId}]]></MsgId>
            </xml>
            """
        return XmlForm.format(**self.__dict)


class ImageMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId, PicUrl, MsgId):
        super().__init__()
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId
        self.__dict['PicUrl'] = PicUrl
        self.__dict['MsgId'] = MsgId

    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[image]]></MsgType>
                <PicUrl><![CDATA[{PicUrl}]]></PicUrl>
                <Image>
                <MediaId><![CDATA[{MediaId}]]></MediaId>
                </Image>
                <MsgId><![CDATA[{MsgId}]]></MsgId>
            </xml>
            """
        return XmlForm.format(**self.__dict)


class VoiceMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId, Format, MsgId, Recognition):
        super().__init__()
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId
        self.__dict['Format'] = Format
        self.__dict['MsgId'] = MsgId
        self.__dict['Recognition'] = Recognition

    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType>< ![CDATA[voice] ]></MsgType>
                <Voice>
                    <MediaId><![CDATA[{MediaId}]]></MediaId>
                </Voice>
                <Format><![CDATA[{Format}]]></Format>
                <Recognition>< ![CDATA[{Recognition}] ]></Recognition>
                <MsgId><![CDATA[{MsgId}]]></MsgId>
            </xml>
            """
        return XmlForm.format(**self.__dict)


class VideoMsg(Msg):
    def __init__(self, toUserName, fromUserName, MediaId, ThumbMediaId, MsgId):
        super().__init__()
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = MediaId
        self.__dict['ThumbMediaId'] = ThumbMediaId
        self.__dict['MsgId'] = MsgId

    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[video]]></MsgType>
                <Video>
                    <MediaId><![CDATA[{MediaId}]]></MediaId>
                    <Title><![CDATA[title]]></Title>
                    <Description><![CDATA[description]]></Description>
                </Video>
                <ThumbMediaId><![CDATA[{ThumbMediaId}]]></ThumbMediaId>
                <MsgId><![CDATA[{MsgId}]]></MsgId>
            </xml>
            """
        return XmlForm.format(**self.__dict)


class ShortVideoMsg(Msg):
    def __init__(self, toUserName, fromUserName, MediaId, ThumbMediaId):
        super().__init__()
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = MediaId
        self.__dict['ThumbMediaId'] = ThumbMediaId

    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[shortvideo]]></MsgType>
                <MediaId><![CDATA[{MediaId}]]></MediaId>
                <ThumbMediaId><![CDATA[thumb_media_id]]></ThumbMediaId>
                <MsgId><![CDATA[{MsgId}]]></MsgId>
            </xml>
            """
        return XmlForm.format(**self.__dict)


class LocationMsg(Msg):
    def __init__(self, toUserName, fromUserName, Location_X, Location_Y, Scale, Label, MsgId, MsgType):
        super().__init__()
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Location_X'] = Location_X
        self.__dict['Location_Y'] = Location_Y
        self.__dict['Scale'] = Scale
        self.__dict['Label'] = Label
        self.__dict['MsgId'] = MsgId
        self.__dict['MsgType'] = MsgType

    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[location]]></MsgType>
                <Location_X><![CDATA[{Location_X}]]></Location_X>
                <Location_Y><![CDATA[{Location_Y}]]></Location_Y>
                <Scale>{Scale}</Scale>
                <Label><![CDATA[{Label}]]></Label>
                <MsgId><![CDATA[{MsgId}]]></MsgId>
            </xml>
            """
        return XmlForm.format(**self.__dict)


class LinkMsg(Msg):
    def __init__(self, toUserName, fromUserName, Title, Description, Url, MsgId, MsgType):
        super().__init__()
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Title'] = Title
        self.__dict['Description'] = Description
        self.__dict['Url'] = Url
        self.__dict['MsgId'] = MsgId
        self.__dict['MsgType'] = MsgType

    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[{MsgType}]]></MsgType>
                <Title><![CDATA[{Title}]]></Title>
                <Description><![CDATA[{Description}]]></Description>
                <Url><![CDATA[{Url}]]></Url>
                <MsgId><![CDATA[{MsgId}]]></MsgId>
            </xml>
            """
        return XmlForm.format(**self.__dict)


class MusicMsg(Msg):
    def __init__(self, toUserName, fromUserName, MediaId, MsgType, Title, Description, MusicUrl, HQMusicUrl, ThumbMediaId):
        super().__init__()
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = MediaId
        self.__dict['MsgType'] = MsgType
        self.__dict['Title'] = Title
        self.__dict['Description'] = Description
        self.__dict['MusicUrl'] = MusicUrl
        self.__dict['HQMusicUrl'] = HQMusicUrl
        self.__dict['ThumbMediaId'] = ThumbMediaId

    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[location]]></MsgType>
                <MediaId><![CDATA[{MediaId}]]></MediaId>
                <Music>
                    <Title><![CDATA[{Title}]]></Title>
                    <Description><![CDATA[{Description}]]></Description>
                    <MusicUrl><![CDATA[{MusicUrl}]]></MusicUrl>
                    <HQMusicUrl><![CDATA[{HQMusicUrl}]]></HQMusicUrl>
                    <ThumbMediaId><![CDATA[{ThumbMediaId}]]></ThumbMediaId>
                </Music>
            </xml>
            """
        return XmlForm.format(**self.__dict)


# 一下代码均是验证微信发给开发者的消息解析，而不是发送给粉丝的消息
class ClickMsg(Msg):
    def __init__(self, toUserName, fromUserName, MsgType, Event, EventKey):
        super().__init__()
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MsgType'] = MsgType
        self.__dict['Event'] = Event
        self.__dict['EventKey'] = EventKey

    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[{MsgType}]]></MsgType>
                <Event><![CDATA[{Event}]]></Event>
                <EventKey><![CDATA[{EventKey}]]></EventKey>
            </xml>
            """
        return XmlForm.format(**self.__dict)


class ViewMsg(Msg):
    def __init__(self, toUserName, fromUserName, MsgType, Event, EventKey, MenuId):
        super().__init__()
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MsgType'] = MsgType
        self.__dict['Event'] = Event
        self.__dict['EventKey'] = EventKey
        self.__dict['MenuId'] = MenuId

    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[{MsgType}]]></MsgType>
                <Event><![CDATA[{Event}]]></Event>
                <EventKey><![CDATA[{EventKey}]]></EventKey>
                <MenuId>{MenuId}</MenuId>
            </xml>
            """
        return XmlForm.format(**self.__dict)


class SubscribeMsg(Msg):
    def __init__(self, toUserName, fromUserName, MsgType, Event, EventKey):
        super().__init__()
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MsgType'] = MsgType
        self.__dict['Event'] = Event
        self.__dict['EventKey'] = EventKey

    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[{MsgType}]]></MsgType>
                <Event><![CDATA[{Event}]]></Event>
                <EventKey><![CDATA[{EventKey}]]></EventKey>
            </xml>
            """
        return XmlForm.format(**self.__dict)


class LOCATIONMSG(Msg):
    def __init__(self, toUserName, fromUserName, MsgType, Event, Latitude, Longitude, Precision):
        super().__init__()
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['MsgType'] = MsgType
        self.__dict['Event'] = Event
        self.__dict['Latitude'] = Latitude
        self.__dict['Longitude'] = Longitude
        self.__dict['Precision'] = Precision
        self.__dict['CreateTime'] = int(time.time())

    def send(self):
        XmlForm = """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[{MsgType}]]></MsgType>
                <Event><![CDATA[{Event}]]></Event>
                <Latitude><![CDATA[{Latitude}]]></Latitude>
                <Longitude><![CDATA[{Longitude}]]></Longitude>
                <Precision><![CDATA[{Precision}]]></Precision>
            </xml>
            """
        return XmlForm.format(**self.__dict)


