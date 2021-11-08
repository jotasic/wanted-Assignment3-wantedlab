
from .base   import *

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'secrect_key')
DEBUG      = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('SQL_DATABASE_NAME', 'wantedlab'),
        'USER': os.environ.get('SQL_USER', 'wantedlab'),
        'PASSWORD': os.environ.get('SQL_PASSWORD', 'wantedlab'),
        'HOST': os.environ.get('SQL_HOST', 'localhost'),
        'PORT': os.environ.get('SQL_PORT', 5432),
    }
}