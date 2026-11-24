from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

UserModel = get_user_model()

@admin.register(UserModel)
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = get_user_model()
    list_display = ['email', 'username', 'is_active','is_staff', ]
    list_filter = ['is_staff', 'is_active', ]
    search_fields = ['email', 'username']
    ordering = ['email', ]
    fieldsets = [
        (
            'Personal Info:',
            {'fields': ('email', 'username', 'password')}
        ),
        (
            'Permissions:',
            {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}
        ),
        (
            None,
            {'fields': ('last_login',)}
        ),
    ]
    add_fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'username',
                'password1',
                'password2',
                'is_staff',
                'is_superuser',
                'is_active',
            ),
        }),
    ]
