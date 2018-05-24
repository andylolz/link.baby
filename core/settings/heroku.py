from .base import *

import django_heroku


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

django_heroku.settings(locals())
