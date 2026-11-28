from django import forms
from django.forms.models import inlineformset_factory
from .models import Recipe, RecipeIngredient, RecipeStep
from GatherAndTaste.mixins import DisabledFieldsFormMixin


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['author', 'slug', 'created_at', 'updated_at']

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Enter the title of your recipe here.",
                "autofocus": True,
            }),
            "servings": forms.NumberInput(attrs={
                "placeholder": "Enter the number of servings."
            }),
            "prep_time_minutes": forms.NumberInput(attrs={
                "placeholder": "Preparation time (in minutes)."
            }),
            "cook_time_minutes": forms.NumberInput(attrs={
                "placeholder": "Cooking time (in minutes)."
            }),
        }


class RecipeCreateForm(RecipeBaseForm):
    pass


class RecipeEditForm(RecipeBaseForm):
    pass


class RecipeDeleteForm(RecipeBaseForm, DisabledFieldsFormMixin):
    pass


IngredientFormSet = inlineformset_factory(
    parent_model=Recipe,
    model=RecipeIngredient,
    fields=["quantity", "unit", "name"],
    extra=1,
    can_delete=True,
)

StepFormSet = inlineformset_factory(
    parent_model=Recipe,
    model=RecipeStep,
    fields=["order", "description", "image"],
    extra=1,
    can_delete=True,
)