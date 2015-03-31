# -*- coding: utf-8 -*-
"""
    Setting for production env

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
#Flake8: noqa
from common import *

STATIC_ROOT = '/opt/pursuite/www/static'
MEDIA_ROOT = '/opt/pursuite/www/media'
ALLOWED_HOSTS = ['pursuite.openlabs.us']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pursuite',
        'USER': 'mysqluser',
        'PASSWORD': 'mysqlpassword',
        'HOST': 'pursuite.c6ga5pe5mdoq.ap-southeast-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}

# Email Settings
EMAIL_USE_TLS = False
EMAIL_HOST = 'mailtrap.io'
EMAIL_PORT = 2525
EMAIL_HOST_USER = 'nasscom-5ae7880ac967ae5d'
EMAIL_HOST_PASSWORD = 'eb5073db7bdb7af1'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Raven configuration
# Set your DSN value
RAVEN_CONFIG = {
    'dsn': 'http://e542381309e640bebb79ae26123e52e5:' + \
            '85869376ce9143a699ed05d07b552059@sentry.openlabs.co.in/22',
}

# Add amazon s3 as a storage mechanism
INSTALLED_APPS += ('storages', 's3_folder_storage',)
DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
DEFAULT_S3_PATH = "media"
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = "AKIAIBGU6ZPMYAHTFOWQ"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "pursuite"
AWS_QUERYSTRING_AUTH = False

MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
MEDIA_URL = '//s3.amazonaws.com/%s/media/' % AWS_STORAGE_BUCKET_NAME
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Setup caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
