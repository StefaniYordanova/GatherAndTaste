from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .validators import PermittedCharacters
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )
    username = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            PermittedCharacters(),
        ],
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_staff = models.BooleanField(
        default=True,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.email
