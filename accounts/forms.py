from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Profile
from GatherAndTaste.mixins import DisabledFieldsFormMixin

UserModel = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['email', 'username', 'phone_number']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'first_name', 'last_name', 'bio']
        widgets = {
            "profile_picture": forms.FileInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last name"}),
            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Tell the community a bit about yourself...",
                }
            ),
        }


class BaseUserPersonalInfoForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['email', 'username', 'phone_number']


class UserPersonalInfoEditForm(BaseUserPersonalInfoForm):
    ...


class UserDeleteForm(BaseUserPersonalInfoForm, DisabledFieldsFormMixin):
    ...