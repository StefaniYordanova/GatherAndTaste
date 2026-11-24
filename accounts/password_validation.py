from django.core.exceptions import ValidationError


class SecurePassword:
    SPECIAL_CHARACTERS = ['_', '*', '$', '#', '&', '%', '.']

    def validate(self, password: str, user=None) -> ValidationError | None:
        if (
                not any(ch.isdigit() for ch in password)
                or not any(ch.islower() for ch in password)
                or not any(ch.isupper() for ch in password)
                or not any(ch in SecurePassword.SPECIAL_CHARACTERS for ch in password)
        ):
            raise ValidationError(
                "Password must contain at least 1 uppercase letter, "
                "1 lowercase letter, 1 digit and 1 special character "
                "('_', '*', '$', '#', '&', '%' or '.')!"
            )

    def get_help_text(self) -> str:
        return (
            "Your password must contain at least 1 uppercase letter, "
            "1 lowercase letter, 1 digit and 1 special character ('_', '*', '$', '#', '&', '%' or '.')."
        )