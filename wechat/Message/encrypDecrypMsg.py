class EncrypDecrypMsg:
    """
    参考：https://blog.csdn.net/szuzsq/article/details/51887012
    说明：
        只有被动回复消息
        (即粉丝向公众号发送消息,
        由微信服务器向公众号服务器转发xml结构,
        同时公众号服务器返回xml结构,
        由微信服务器转发给粉丝)可以设置加密.
        其他3种消息(群发消息,客服消息,模板消息)的调用因为是API调用而不是对请求的返回,所以不需要加解密.
    """

    def __init__(self):
        pass


#################### 加解密 ####################
import base64
import string
import random
import hashlib
import time
import struct
from Crypto.Cipher import AES
import xml.etree.cElementTree as ET
import sys
import socket
from binascii import b2a_hex, a2b_hex

import importlib
importlib.reload(sys)


"""
关于Crypto.Cipher模块，ImportError: No module named 'Crypto'解决方案
请到官方网站 https://www.dlitz.net/software/pycrypto/ 下载pycrypto。
下载后，按照README中的“Installation”小节的提示进行pycrypto安装。
"""


class FormatException(Exception):
    pass


def throw_exception(message, exception_class=FormatException):
    """my define raise exception function"""
    raise exception_class(message)


class SHA1:
    """
    计算公众平台的消息签名接口
    """

    def getSHA1(self, token, timestamp, nonce, encrypt):
        """用SHA1算法生成安全签名
        @param token:  票据
        @param timestamp: 时间戳
        @param encrypt: 密文
        @param nonce: 随机字符串
        @return: 安全签名
        """
        try:
            sortlist = [token, timestamp, nonce, encrypt]
            sortlist.sort()
            sha = ''.join([s for s in sortlist])
            sha = hashlib.sha1(sha.encode("utf-8"))
            return sha.hexdigest()
        except Exception as e:
            print(e)
            return None


class XMLParse:
    """
    提供提取消息格式中的密文及生成回复消息格式的接口
    """
    # xml消息模板
    AES_TEXT_RESPONSE_TEMPLATE = """
    <xml>
        <Encrypt><![CDATA[%(msg_encrypt)s]]></Encrypt>
        <MsgSignature><![CDATA[%(msg_signaturet)s]]></MsgSignature>
        <TimeStamp>%(timestamp)s</TimeStamp>
        <Nonce><![CDATA[%(nonce)s]]></Nonce>
    </xml>"""

    def extract(self, xmltext):
        """提取出xml数据包中的加密消息
        @param xmltext: 待提取的xml字符串
        @return: 提取出的加密消息字符串
        """
        try:
            xml_tree = ET.fromstring(xmltext)
            encrypt = xml_tree.find("Encrypt")
            touser_name = xml_tree.find("ToUserName")
            return encrypt.text, touser_name.text
        except Exception as e:
            print(e)
            return None, None

    def generate(self, encrypt, signature, timestamp, nonce):
        """生成xml消息
        @param encrypt: 加密后的消息密文
        @param signature: 安全签名
        @param timestamp: 时间戳
        @param nonce: 随机字符串
        @return: 生成的xml字符串
        """
        resp_dict = {
            'msg_encrypt': encrypt,
            'msg_signaturet': signature,
            'timestamp': timestamp,
            'nonce': nonce,
        }
        resp_xml = self.AES_TEXT_RESPONSE_TEMPLATE % resp_dict
        return resp_xml


class PKCS7Encoder:
    """提供基于PKCS7算法的加解密接口"""

    block_size = 32

    def encode(self, text):
        """ 对需要加密的明文进行填充补位
        @param text: 需要进行填充补位操作的明文
        @return: 补齐明文字符串
        """
        text_length = len(text)
        # 计算需要填充的位数
        amount_to_pad = self.block_size - (text_length % self.block_size)
        if amount_to_pad == 0:
            amount_to_pad = self.block_size
        # 获得补位所用的字符
        pad = chr(amount_to_pad)
        return text + pad * amount_to_pad

    def decode(self, decrypted):
        """删除解密后明文的补位字符
        @param decrypted: 解密后的明文
        @return: 删除补位字符后的明文
        """
        pad = ord(decrypted[-1])
        if pad < 1 or pad > 32:
            pad = 0
        return decrypted[:-pad]


class Prpcrypt(object):
    """提供接收和推送给公众平台消息的加解密接口"""

    def __init__(self, key):
        # self.key = base64.b64decode(key+"=")
        self.key = key
        # 设置加解密模式为AES的CBC模式
        self.mode = AES.MODE_CBC

    def encrypt(self, text, appid):
        """对明文进行加密
        @param text: 需要加密的明文
        @return: 加密得到的字符串
        """
        # 16位随机字符串添加到明文开头
        text = self.get_random_str() + struct.pack("I", socket.htonl(len(text))).decode() + text + appid
        # 使用自定义的填充方式对明文进行补位填充
        pkcs7 = PKCS7Encoder()
        text = pkcs7.encode(text)
        # 加密
        cryptor = AES.new(self.key, self.mode, self.key[:16])

        try:
            ciphertext = cryptor.encrypt(text)
            # 使用BASE64对加密后的字符串进行编码
            return base64.b64encode(ciphertext)
        except Exception as e:
            print('e', e)
            return None

    def decrypt(self, text, appid):
        """对解密后的明文进行补位删除
        @param text: 密文
        @return: 删除填充补位后的明文
        """
        try:
            cryptor = AES.new(self.key, self.mode, self.key[:16])
            # 使用BASE64对密文进行解码，然后AES-CBC解密
            plain_text = cryptor.decrypt(base64.b64decode(text))
        except Exception as e:
            print(e)
            return None
        try:
            pad = plain_text[-1]
            # 去掉补位字符串
            # pkcs7 = PKCS7Encoder()
            # plain_text = pkcs7.encode(plain_text)
            # 去除16位随机字符串
            content = plain_text[16:-pad]
            xml_len = socket.ntohl(struct.unpack("I", content[: 4])[0])
            xml_content = content[4: xml_len + 4]
            from_appid = content[xml_len + 4:].decode()
        except Exception as e:
            print(e)
            return None
        if from_appid != appid:
            return None

        return 0, xml_content

    def get_random_str(self):
        """ 随机生成16位字符串
        @return: 16位字符串
        """
        rule = string.ascii_letters + string.digits
        str = random.sample(rule, 16)
        return "".join(str)


class WXBizMsgCrypt(object):
    # 构造函数
    # @param sToken: 公众平台上，开发者设置的Token
    # @param sEncodingAESKey: 公众平台上，开发者设置的EncodingAESKey
    # @param sAppId: 企业号的AppId
    def __init__(self, sToken, sEncodingAESKey, sAppId):
        try:
            self.key = base64.b64decode(sEncodingAESKey + "=")
            assert len(self.key) == 32
        except:
            throw_exception("[error]: EncodingAESKey unvalid !", FormatException)
        # return ierror.WXBizMsgCrypt_IllegalAesKey)
        self.token = sToken
        self.appid = sAppId

    def EncryptMsg(self, sReplyMsg, sNonce, timestamp=None):
        # 将公众号回复用户的消息加密打包
        # @param sReplyMsg: 企业号待回复用户的消息，xml格式的字符串
        # @param sTimeStamp: 时间戳，可以自己生成，也可以用URL参数的timestamp,如为None则自动用当前时间
        # @param sNonce: 随机串，可以自己生成，也可以用URL参数的nonce
        # sEncryptMsg: 加密后的可以直接回复用户的密文，包括msg_signature, timestamp, nonce, encrypt的xml格式的字符串,
        # return：成功0，sEncryptMsg,失败返回对应的错误码None
        pc = Prpcrypt(self.key)
        encrypt = pc.encrypt(sReplyMsg, self.appid)
        if timestamp is None:
            timestamp = str(int(time.time()))
        # 生成安全签名
        sha1 = SHA1()
        signature = sha1.getSHA1(self.token, timestamp, sNonce, encrypt)
        xmlParse = XMLParse()
        return xmlParse.generate(encrypt, signature, timestamp, sNonce)

    def DecryptMsg(self, sPostData, sMsgSignature, sTimeStamp, sNonce):
        # 检验消息的真实性，并且获取解密后的明文
        # @param sMsgSignature: 签名串，对应URL参数的msg_signature
        # @param sTimeStamp: 时间戳，对应URL参数的timestamp
        # @param sNonce: 随机串，对应URL参数的nonce
        # @param sPostData: 密文，对应POST请求的数据
        #  xml_content: 解密后的原文，当return返回0时有效
        # @return: 成功0，失败返回对应的错误码
        # 验证安全签名
        xmlParse = XMLParse()
        encrypt, touser_name = xmlParse.extract(sPostData)
        sha1 = SHA1()
        signature = sha1.getSHA1(self.token, sTimeStamp, sNonce, encrypt)
        if not signature == sMsgSignature:
            return None
        pc = Prpcrypt(self.key)
        xml_content = pc.decrypt(encrypt, self.appid)

        return xml_content


#################### 加解密例子 ####################
if __name__ == '__main__':
    """ 
    1.第三方回复加密消息给公众平台；
    2.第三方收到公众平台发送的消息，验证消息的安全性，并对消息进行解密。
    """
    encodingAESKey = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFG"
    to_xml = """
    <xml>
        <ToUserName><![CDATA[oia2TjjewbmiOUlr6X-1crbLOvLw]]></ToUserName>
        <FromUserName><![CDATA[gh_7f083739789a]]></FromUserName>
        <CreateTime>1407743423</CreateTime>
        <MsgType><![CDATA[video]]></MsgType>
        <Video>
            <MediaId><![CDATA[eYJ1MbwPRJtOvIEabaxHs7TX2D-HV71s79GUxqdUkjm6Gs2Ed1KF3ulAOA9H1xG0]]></MediaId>
            <Title><![CDATA[testCallBackReplyVideo]]></Title>
            <Description><![CDATA[testCallBackReplyVideo]]></Description>
        </Video>
    </xml>"""
    token = "spamtest"
    nonce = "1320562132"
    appid = "wx2c2769f8efd9abc2"
    # 测试加密接口
    encryp_test = WXBizMsgCrypt(token, encodingAESKey, appid)
    encrypt_xml = encryp_test.EncryptMsg(to_xml, nonce)
    print('encrypt_xml', encrypt_xml)

    # 测试解密接口
    timestamp = "1409735669"
    msg_sign = "5d197aaffba7e9b25a30732f161a50dee96bd5fa"

    from_xml = """
    <xml>
        <ToUserName><![CDATA[gh_10f6c3c3ac5a]]></ToUserName>
        <FromUserName><![CDATA[oyORnuP8q7ou2gfYjqLzSIWZf0rs]]></FromUserName>
        <CreateTime>1409735668</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[abcdteT]]></Content>
        <MsgId>6054768590064713728</MsgId>
        <Encrypt><![CDATA[hyzAe4OzmOMbd6TvGdIOO6uBmdJoD0Fk53REIHvxYtJlE2B655HuD0m8KUePWB3+LrPXo87wzQ1QLvbeUgmBM4x6F8PGHQHFVAFmOD2LdJF9FrXpbUAh0B5GIItb52sn896wVsMSHGuPE328HnRGBcrS7C41IzDWyWNlZkyyXwon8T332jisa+h6tEDYsVticbSnyU8dKOIbgU6ux5VTjg3yt+WGzjlpKn6NPhRjpA912xMezR4kw6KWwMrCVKSVCZciVGCgavjIQ6X8tCOp3yZbGpy0VxpAe+77TszTfRd5RJSVO/HTnifJpXgCSUdUue1v6h0EIBYYI1BD1DlD+C0CR8e6OewpusjZ4uBl9FyJvnhvQl+q5rv1ixrcpCumEPo5MJSgM9ehVsNPfUM669WuMyVWQLCzpu9GhglF2PE=]]></Encrypt>
    </xml> """
    decrypt_test = WXBizMsgCrypt(token, encodingAESKey, appid)
    decryp_xml = decrypt_test.DecryptMsg(from_xml, msg_sign, timestamp, nonce)
    print('decryp_xml', decryp_xml)

