from os import getenv

import dj_database_url
from dynaconf import settings as _settings

from pathlib import Path
PROJECT_DIR = Path(__file__).parent.resolve()
BASE_DIR = PROJECT_DIR.parent.resolve()
REPO_DIR = BASE_DIR.parent.resolve()


# SECRET_KEY = 'lbt#79-i_9#$^3b8!&#z=c^%z1*b&*m^u$erw*^e3vciini^e5'


SECRET_KEY = _settings.SECRET_KEY

DEBUG = _settings.DEBUG

ALLOWED_HOSTS = _settings.ALLOWED_HOSTS

INTERNAL_IPS = [
    "127.0.0.1",
]

#DEBUG = True

# ALLOWED_HOSTS = [
   # "127.0.0.1",
  #  "localhost",
 #   "samoyed1.herokuapp.com",
# ]




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "apps.index",
    "apps.catalog",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  #наличие переменной в дебаг
                'django.template.context_processors.request',  #в шаблон добавляет в шаблон реквест
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


_db_url = _settings.DATABASE_URL
if _settings.ENV_FOR_DYNACONF == "heroku":
    _db_url = getenv("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.parse(_db_url, conn_max_age=600),
}

#DATABASES = {
   # 'default': {
   #     'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': (BASE_DIR / 'db.sqlite3').as_posix(),
   # }

#}
# {
#     'default': dj_database_url.parse(_db_url, conn_max_age=600),
# -db.sqlite3 - файловая база данных это минус обслуживает один запрос
# - файловые системы на хероку отсутствует


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



STATIC_URL = '/assets/'


STATICFILES_DIRS = [
    PROJECT_DIR / "static",
]

STATIC_ROOT = REPO_DIR / ".static"
