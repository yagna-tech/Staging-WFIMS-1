# -*- coding: utf-8 -*-
"""
    Setting for production env

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
#Flake8: noqa
from common import Common
import os


class Dev(Common):

    #STATIC_ROOT = '/opt/pursuite/www/static'
    #MEDIA_ROOT = '/opt/pursuite/www/media'
    #ALLOWED_HOSTS = ['pursuite.openlabs.us']

    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(Common.PROJECT_PATH, 'pursuite.db')
        }
    }

    # Email Settings
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    # Raven configuration
    # Set your DSN value
    #RAVEN_CONFIG = {
    #    'dsn': '',
    #}


    #MEDIA_URL = '//s3.amazonaws.com/%s/media/' % AWS_STORAGE_BUCKET_NAME
    #ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'


