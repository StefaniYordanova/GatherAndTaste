from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Profile

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
            {'fields': ('email', 'username', 'phone_number', 'password')}
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
                'phone_number',
                'password1',
                'password2',
                'is_staff',
                'is_superuser',
                'is_active',
            ),
        }),
    ]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'last_updated_at']
    list_filter = ['last_updated_at']
    search_fields = ['first_name', 'last_name']
    readonly_fields = ['last_updated_at']
