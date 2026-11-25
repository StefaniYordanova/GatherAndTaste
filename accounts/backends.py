from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class PhoneNumberBackend(ModelBackend):
    def authenticate(
        self, request, username =None, password =None, **kwargs
    ):
        UserModel = get_user_model()

        if not username or not password:
            return

        user = UserModel.objects.filter(
            phone_number=username,
        ).first()

        if not user:
            return

        if user.check_password(password) and self.user_can_authenticate(user):
            return user

