import os

#settings.pyからそのままコピー
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-31bkt1vw8_st@rqq2c069q9ogt")"#m%pp")"x@#@gf1")""("n0g030b")"' #追加
DEBUG = True #ローカルでDebugできるようになります

#settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = []

DEBUG = True