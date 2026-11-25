from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

UserModel = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['email', 'username', 'phone_number']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'
