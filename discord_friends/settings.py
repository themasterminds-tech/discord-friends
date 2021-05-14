# Project settings

from pathlib import Path
import os
from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config('SECRET_KEY', cast=str)


DEBUG = True


ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Project applications
    'contacts',

    # 3rd party libraries
    'pwa',
    'sslserver'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'discord_friends.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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


WSGI_APPLICATION = 'discord_friends.wsgi.application'

"""
Uncomment the section below to use the
default database for the project
"""

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', cast=str),
        'USER': config('DB_USER', cast=str),
        'PASSWORD': config('DB_PASSWORD', cast=str),
        'HOST': config('DB_HOST', cast=str),
        'PORT': config('DB_PORT', cast=int),
    }
}


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


LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'UTC'


USE_I18N = True


USE_L10N = True


USE_TZ = True


STATIC_URL = '/static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'downloads')
]


PWA_SERVICE_WORKER_PATH = os.path.join(
    BASE_DIR, 'static/shared/js', 'worker.js')

PWA_APP_NAME = config('PWA_APP_NAME', cast=str)
PWA_APP_DESCRIPTION = config('PWA_APP_DESCRIPTION', cast=str)
PWA_APP_THEME_COLOR = config('PWA_APP_THEME_COLOR', cast=str)
PWA_APP_BACKGROUND_COLOR = config('PWA_APP_BACKGROUND_COLOR', cast=str)
PWA_APP_DISPLAY = config('PWA_APP_DISPLAY', cast=str)
PWA_APP_SCOPE = config('PWA_APP_SCOPE', cast=str)
PWA_APP_ORIENTATION = config('PWA_APP_ORIENTATION', cast=str)
PWA_APP_START_URL = config('PWA_APP_START_URL', cast=str)
PWA_APP_STATUS_BAR_COLOR = config('PWA_APP_STATUS_BAR_COLOR', cast=str)

PWA_APP_ICONS = [
    {
        'src': 'static/shared/img/web/discord-256x256.png',
        'sizes': '256x256',
        'type': 'image/png'
    },
    {
        'src': 'static/shared/img/web/discord-128x128.png',
        'sizes': '128x128',
        'type': 'image/png'
    },
    {
        'src': 'static/shared/img/web/discord-64x64.png',
        'sizes': '64x64',
        'type': 'image/png'
    },
    {
        'src': 'static/shared/img/web/discord-48x48.png',
        'sizes': '48x48',
        'type': 'image/png'
    },
    {
        'src': 'static/shared/img/web/discord-32x32.png',
        'sizes': '32x32',
        'type': 'image/png'
    },
    {
        'src': 'static/shared/img/web/discord-16x16.png',
        'sizes': '16x16',
        'type': 'image/png'
    },
]

PWA_APP_SPLASH_SCREEN = [
    {
        'src': 'static/shared/img/web/discord-256x256.png',
        'sizes': '256x256',
        'type': 'image/png'
    }
]

PWA_APP_DIR = config('PWA_APP_DIR', cast=str)
PWA_APP_LANG = config('PWA_APP_LANG', cast=str)
