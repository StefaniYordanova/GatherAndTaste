from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class PermittedCharacters:
    PERMITTED_CHARACTERS = ['_', '.', '@', '&', ]

    def __call__(self, value: str) -> ValidationError | None:
        if not all(
            ch.isalnum() or ch in PermittedCharacters.PERMITTED_CHARACTERS
            for ch in value
        ):
            raise ValidationError(
                "The username must consist only of letters, "
                "numbers, '_', '.', '@' and '&'!"
            )