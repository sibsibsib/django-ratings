import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'djangoratings.db'),
    }
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',

    'djangoratings',
    'djangoratings.tests',
]

SECRET_KEY = '@#D43290fsm$edfiojag8xfg'
ROOT_URLCONF = ''
