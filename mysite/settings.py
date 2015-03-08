# -*- coding: utf-8 -*-
"""
Django settings for proj_django_blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oy-n+rtle94@f%ox1^u!4h40xnkv(+ik3xx=vyr*+aw#xt_pxd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if config.MODE == config.MODE_DEV else False

TEMPLATE_DEBUG = True if config.MODE == config.MODE_DEV else False

if config.MODE == config.MODE_PRO:
    ALLOWED_HOSTS = ['ak47ok.com']
else:
    ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if config.MODE == config.MODE_PRO:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': "proj_blog",
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
elif config.MODE == config.MODE_DEV:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': "proj_blog",
            'USER': 'postgres',
            'PASSWORD': '123456',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-ch'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)


##############################################################
# logger configure
##############################################################
WEB_LOG_FILE_PATH = os.path.join(BASE_DIR, "logs/site.log")
WORKER_LOG_FILE_PATH = os.path.join(BASE_DIR, "logs/worker.log")

WORKER_LOG_LEVEL = 'DEBUG'

LOG_FORMAT = '\n'.join((
    '/' + '-' * 80,
    '[%(levelname)s][%(asctime)s][%(process)d:%(thread)d][%(filename)s:%(lineno)d %(funcName)s]:',
    '%(message)s',
    '-' * 80 + '/',
))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'formatters': {
        'standard': {
            'format': LOG_FORMAT,
        },
    },

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': lambda x: DEBUG,
        }
    },
    'handlers': {

        'rotating_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': WEB_LOG_FILE_PATH,
            'maxBytes': 1024*1024*500,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'worker_file': {
            'level': WORKER_LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': WORKER_LOG_FILE_PATH,
            'maxBytes': 1024*1024*500,
            'backupCount': 5,
            'formatter': 'standard',
            },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },

    },
    'loggers': {
        'django': {
            'handlers': ['rotating_file'],
            'level': 'DEBUG',
            'propagate': False
        },

        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },

        'worker': {
            'handlers': ['console', 'worker_file'],
            'level': WORKER_LOG_LEVEL,
            'propagate': False
        },
    }
}
