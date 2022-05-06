from django.db import models


# Create your models here.
class Wechat(models.Model):
    STATE_CHOICES = (
        ('0', '关注中'),
        ('1', '取关中')
    )

    id = models.AutoField(primary_key=True, verbose_name='主键ID')
    CreateTime = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='关注时间/取关时间')
    FromUserName = models.CharField(max_length=30,  null=False, verbose_name='粉丝')
    ToUserName = models.CharField(max_length=30,  null=False, verbose_name='公众号')
    state = models.IntegerField(null=False, verbose_name="状态", choices=STATE_CHOICES)

    class Meta:
        db_table = 'wechat_fans'
        verbose_name = '公众号粉丝'
        verbose_name_plural = verbose_name


class WechatWeb(models.Model):
    SEX_CHOICES = (
        ('0', '未知'),
        ('1', '男性'),
        ('2', '女性'),
    )
    id = models.AutoField(primary_key=True, verbose_name='主键ID')
    CreateTime = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='授权时间')
    openid = models.CharField(max_length=300, blank=True, null=True, verbose_name='用户唯一标识')
    nickname = models.CharField(max_length=300, blank=True, null=True, verbose_name='用户昵称')
    sex = models.IntegerField(null=False, choices=SEX_CHOICES, verbose_name='性别')
    language = models.CharField(max_length=300, blank=True, null=True, verbose_name='语言')
    city = models.CharField(max_length=300, blank=True, null=True, verbose_name='城市')
    province = models.CharField(max_length=300, blank=True, null=True, verbose_name='省份')
    country = models.CharField(max_length=300, blank=True, null=True, verbose_name='国家')
    headimgurl = models.CharField(max_length=500, blank=True, null=True, verbose_name='头像')
    privilege = models.CharField(max_length=300, blank=True, null=True, verbose_name='用户特权信息')

    class Meta:
        db_table = 'web_authorization_user'
        verbose_name = '网页授权的用户'
        verbose_name_plural = verbose_name


class WechatFansLocation(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='主键ID')
    CreateTime = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='授权时间')
    FromUserName = models.CharField(max_length=30, null=False, verbose_name='公众号')
    ToUserName = models.CharField(max_length=30, null=False, verbose_name='粉丝')
    Latitude = models.FloatField(max_length=100, null=False, verbose_name='纬度')
    Longitude = models.FloatField(max_length=100, null=False, verbose_name='经度')
    Precision = models.FloatField(max_length=100, null=False, verbose_name='精度')

    class Meta:
        db_table = 'wechat_location'
        verbose_name = '粉丝位置信息'
        verbose_name_plural = verbose_name

    pass

