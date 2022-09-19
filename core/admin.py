from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from core.models import Profile


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            # 'fields': ('username', 'password', 'email', 'first_name', 'last_name', 'is_active', 'is_superuser', 'is_staff', 'user_permissions', 'groups', )
            'fields': ('username', 'password', 'email', 'is_staff', 'groups')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('user_permissions', 'is_active', 'is_superuser', )
        }),
    )
    list_display = ('username', 'email', )
    list_filter = ('is_staff', 'is_active', )
    search_fields = ('last_name__startswith', )

    class Meta:
        ordering = ('date_joined', )

admin.site.register(get_user_model(), UserAdmin)
admin.site.register(Profile)