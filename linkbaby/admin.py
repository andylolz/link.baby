from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import LinkbabyUser


admin.site.register(LinkbabyUser, UserAdmin)
