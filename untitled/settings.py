"""
Django settings for untitled project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f43ldqoiw47n_eem_d&+dv%w$gje_p)fvcnfg+^xmlg_8jgwfl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DB_start'

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

ROOT_URLCONF = 'untitled.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
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

WSGI_APPLICATION = 'untitled.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

#
# ['/Users/marcus/PycharmProjects/untitled',
#  '/private/var/folders/yk/mn8vp4_s3dqdpmqzcjlxll_00000gn/T/AppTranslocation/F3B87009-9757-4ADE-B07D-13FCF0AF2FD5/d/PyCharm.app/Contents/helpers/pydev',
#  '/private/var/folders/yk/mn8vp4_s3dqdpmqzcjlxll_00000gn/T/AppTranslocation/F3B87009-9757-4ADE-B07D-13FCF0AF2FD5/d/PyCharm.app/Contents/helpers/pydev',
#  '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip',
#  '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6',
#  '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload',
#  '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages',
#  '/Users/marcus/PycharmProjects/untitled',
#  '/private/var/folders/yk/mn8vp4_s3dqdpmqzcjlxll_00000gn/T/AppTranslocation/F3B87009-9757-4ADE-B07D-13FCF0AF2FD5/d/PyCharm.app/Contents/helpers/pycharm',
#  '/private/var/folders/yk/mn8vp4_s3dqdpmqzcjlxll_00000gn/T/AppTranslocation/F3B87009-9757-4ADE-B07D-13FCF0AF2FD5/d/PyCharm.app/Contents/helpers/pydev']
