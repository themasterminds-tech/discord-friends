from django.contrib import admin
from .models import Friends


class FriendsAdmin(admin.ModelAdmin):
    list_display = ['username', 'tag', 'user_id', 'account']
    list_filter = ['account']


admin.site.register(Friends, FriendsAdmin)
