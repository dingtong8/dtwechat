"""
Django settings for dtwechat project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import sys
from configparser import ConfigParser
from pathlib import Path


# =================== 配置文件读取 ===================
CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))
conf = ConfigParser()
conf.read('{0}/config.ini'.format(CONFIG_DIR))


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5ahd&10x_jb#)z2zi!j#g362j&slim!xz#l-xuj5$m0m@d_s7p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wechat.apps.WechatConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dtwechat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dtwechat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ====================== 微信服务号相关设置 ======================
TOKEN = conf.get("WX_DATA_STORE", "TOKEN")
APP_ID = conf.get("WX_DATA_STORE", "APP_ID")
APP_SECRET = conf.get("WX_DATA_STORE", "APP_SECRET")


# ====================== redis 相关设置 ======================
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": conf.get("REDIS", "LOCATION").__str__().format("0"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 200},
            # "PASSWORD": "密码",  # 可不写，密码
            # "DECODE_RESPONSES": True  # 可不写，redis get的数据是字符串格式(unicode，而不是bytes)
        }
    },
    "access_token": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": conf.get("REDIS", "LOCATION").__str__().format("1"),
        "OPTIONS": {
            "CONNECTION_POOL_KWARGS": {"max_connections": 200}
        }
    },
    "session_cache": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": conf.get("REDIS", "LOCATION").__str__().format("2"),
        "OPTIONS": {
            "CONNECTION_POOL_KWARGS": {"max_connections": 200},
            # "SERIALIZER": "django_redis.serializers.json.JSONSerializer",
        }
    }
}


SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

