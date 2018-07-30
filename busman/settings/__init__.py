"""
Django settings for busman project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os


# App settings
SCHOOL = ""  # string: school name


# Django settings overrides
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/app/"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'menmi2ehu0*91ta#xho_scz+1dtzv=*+dz5c7r05fz6h#@+@$w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'pipeline',
    'channels',
    'jsonify',
    'busman.apps.usermgmt',
    'busman.apps.busmap'
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

ROOT_URLCONF = 'busman.urls'

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

ASGI_APPLICATION = "busman.asgi.application"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],
        },
    },
}
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "collected_static")
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    'STYLESHEETS': {
        'base': {
            'source_filenames': (
                'css/vendor/normalize.css',
                'css/base.scss',
            ),
            'output_filename': 'css/base.css'
        },
        'login': {
            'source_filenames': (
                'css/usermgmt/login.scss',
            ),
            'output_filename': 'css/login.css'
        },
        'busmap': {
            'source_filenames': (
                'css/busmap/busmap.scss',
            ),
            'output_filename': 'css/busmap.css'
        }
    },
    'JAVASCRIPT': {
        'login': {
            'source_filenames': (
                'js/usermgmt/login.browserify.js',
            ),
            'output_filename': 'js/login.js'
        },
        'busmap': {
            'source_filenames': (
                'js/busmap/map.browserify.js',
            ),
            'output_filename': 'js/busmap.js'
        }
    }
}
if DEBUG:
    PIPELINE['BROWSERIFY_ARGS'] = ['-d']
else:
    PIPELINE['BROWSERIFY_ARGS'] = []
# vueify
PIPELINE['BROWSERIFY_ARGS'] += '--transform [ vueify ]'.split()

PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE['COMPILERS'] = (
    'pipeline.compilers.sass.SASSCompiler',
    'pipeline_browserify.compiler.BrowserifyCompiler',
)

if os.getenv('SASS_BINARY'):
    PIPELINE['SASS_BINARY'] = os.getenv('SASS_BINARY')
if os.getenv('BROWSERIFY_BINARY'):
    PIPELINE['BROWSERIFY_BINARY'] = os.getenv('BROWSERIFY_BINARY')

from .secret import *  # noqa
