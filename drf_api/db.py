from drf_api.env import config
import os


DB_NAME = config('DATABASE_NAME', default=None)
DB_USER = config('DATABASE_USER', default=None)
DB_PASSWORD = config('DATABASE_PASSWORD', default=None)
DB_HOST = config('DATABASE_HOST', default=None)
DB_PORT = int(config('DATABASE_PORT', default=None))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}