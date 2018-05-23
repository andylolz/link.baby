from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.conf import settings
from django.apps import apps


admin.site.register(apps.get_model(settings.AUTH_USER_MODEL), UserAdmin)
