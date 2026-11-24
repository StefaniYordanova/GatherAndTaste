from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(
        self, request, username = ..., password = ..., **kwargs
    ):
        if not username or not password:
            return

        user = UserModel.objects.filter(
            email=username,
        ).first()

        if not user:
            return

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
