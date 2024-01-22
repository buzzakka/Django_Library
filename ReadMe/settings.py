from pathlib import Path
from dotenv import dotenv_values
import os

# config - секретрные данные из файла .env
config = dotenv_values(".env")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config.get("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ['*',]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Catalog.apps.CatalogConfig',
    'users.apps.UsersConfig',
    'api.apps.ApiConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
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

ROOT_URLCONF = 'ReadMe.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'ReadMe.wsgi.application'

DATABASES = {
   'default': {
       'ENGINE':    'django.db.backends.postgresql',
       'NAME':      config['DB_NAME'],
       'USER':      config['DB_USER'],
       'PASSWORD':  config['DB_PASSWORD'],
       'HOST':      config['DB_HOST'],
       'PORT':      config['DB_PORT'],
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

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    'users.authentication.EmailAuthBackend',
]

AUTH_USER_MODEL = "users.User"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

LOGIN_REDIRECT_URL = "/users/login/"
LOGIN_URL = "/users/login/"
