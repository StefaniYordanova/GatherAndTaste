from decimal import Decimal

from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify
from GatherAndTaste.settings import AUTH_USER_MODEL
from .choices import Tag, Difficulty, Visibility, IngredientUnit

# TODO: Make migrations and migrate!

class Recipe(models.Model):
    author = models.ForeignKey(
        to=AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='recipes',
    )
    title = models.CharField(
        max_length=50,
    )
    visibility = models.CharField(
        max_length=10,
        choices=Visibility.choices,
        default=Visibility.PUBLIC,
    )
    tag = models.CharField(
        max_length=20,
        choices=Tag.choices,
        blank=True,
        null=True,
    )
    difficulty_level = models.CharField(
        max_length=10,
        choices=Difficulty.choices,
        default=Difficulty.EASY,
    )
    image = models.ImageField(
        upload_to='recipes_images/',
        blank=True,
        null=True,
    )
    servings = models.PositiveIntegerField(
        default=4,
    )
    prep_time_minutes = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    cook_time_minutes = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
    )
    created_at = models.DateField(
        auto_now_add=True,
    )
    updated_at = models.DateField(
        auto_now=True,
    )

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_parts = [self.title]
            if self.tag:
                slug_parts.append(self.tag)
            self.slug = slugify('-'.join(slug_parts))

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        to='Recipe',
        on_delete=models.CASCADE,
        related_name='ingredients',
    )
    name = models.CharField(
        max_length=40,
    )
    quantity = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=Decimal("0.00"),
    )
    unit = models.CharField(
        max_length=15,
        choices=IngredientUnit.choices,
        blank=True,
        null=True,
    )


class RecipeStep(models.Model):
    recipe = models.ForeignKey(
        to='Recipe',
        on_delete=models.CASCADE,
        related_name="steps",
    )
    order = models.PositiveIntegerField(
        default=1,
    )
    description = models.TextField(
        validators=[
            MinLengthValidator(5),
        ],
    )
    image = models.ImageField(
        upload_to="recipes_steps/",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"Step {self.order}: {self.recipe.title}"
