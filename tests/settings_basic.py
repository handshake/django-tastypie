from settings import *
INSTALLED_APPS.append('django.contrib.sessions')
INSTALLED_APPS.append('basic')

MIDDLEWARE_CLASSES.append('django.contrib.sessions.middleware.SessionMiddleware')
MIDDLEWARE_CLASSES.append('django.contrib.auth.middleware.AuthenticationMiddleware')

ROOT_URLCONF = 'basic.urls'
