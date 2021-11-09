
from .base   import *

ALLOWED_HOSTS = ['*']

SECRET_KEY = get_env_variable_or('DJANGO_SECRET_KEY')
DEBUG      = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_env_variable_or('SQL_DATABASE_NAME'),
        'USER': get_env_variable_or('SQL_USER'),
        'PASSWORD': get_env_variable_or('SQL_PASSWORD'),
        'HOST': get_env_variable_or('SQL_HOST'),
        'PORT': get_env_variable_or('SQL_PORT'),
    }
}