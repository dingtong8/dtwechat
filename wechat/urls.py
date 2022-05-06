from django.conf.urls import url
from . import views


app_name = 'wechat'

urlpatterns = [
    url(r'main/', views.weixin_main, name='weixin_main'),
    url(r'index/', views.index, name='index'),
    url(r'get_signature/', views.get_signature, name='get_signature'),
]


