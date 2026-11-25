from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from GatherAndTaste import settings
from .validators import PermittedCharacters, PhoneNumberValidator
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
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            PhoneNumberValidator(),
        ],
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    profile_picture = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True,
    )
    first_name = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )
    bio = models.TextField(
        blank=True,
        null=True,
    )
    last_updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
