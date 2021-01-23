from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
]

# INSTALLED_APPS += [
#     '',
# ]


MIDDLEWARE += [
    'whitenoise.middleware.WhitenoiseMiddleware',
]

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
