from django.contrib import admin
from .models import Friends


class FriendsAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'username', 'tag']


admin.site.register(Friends, FriendsAdmin)
