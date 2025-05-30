from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.sessions.models import Session

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ['username', 'email', 'is_active', 'is_staff', 'is_superuser']

    ordering = ['username']

    # Add your extra fields here (like role, degree, etc.) in fieldsets
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'role', 'degree', 'faculty', 'department', 'university', 'city', 'country', 'personal_webpage')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
admin.site.register(Session)
admin.site.register(CustomUser, CustomUserAdmin)
