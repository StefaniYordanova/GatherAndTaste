from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm, IngredientFormSet, StepFormSet
from .models import Recipe


def _handle_recipe_form_with_formsets(
        request,
        form_class,
        template_name,
        recipe=None
    ):
    editable = recipe is not None

    form = form_class(
        request.POST or None,
        request.FILES or None,
        instance=recipe,
    )
    ingredient_formset = IngredientFormSet(
        request.POST or None,
        instance=recipe,
        prefix="ingredients",
    )
    step_formset = StepFormSet(
        request.POST or None,
        request.FILES or None,
        instance=recipe,
        prefix="steps",
    )

    if request.method == 'POST':
        form_valid = form.is_valid()
        ingredients_valid = ingredient_formset.is_valid()
        steps_valid = step_formset.is_valid()

        if form_valid and ingredients_valid and steps_valid:
            with transaction.atomic():
                saved_recipe = form.save(commit=False)

                if not editable:
                    saved_recipe.author = request.user

                saved_recipe.save()

                ingredient_formset.instance = saved_recipe
                ingredient_formset.save()

                step_formset.instance = saved_recipe
                step_formset.save()

            return redirect('common:home')

    context = {
        "form": form,
        "ingredient_formset": ingredient_formset,
        "step_formset": step_formset,
        "editable": editable,
        "recipe": recipe,
    }

    return render(request, template_name, context=context)


@login_required
def recipe_create_view(request: HttpRequest):
    return _handle_recipe_form_with_formsets(
        request=request,
        form_class=RecipeCreateForm,
        template_name='recipes/add-recipe-page.html',
    )


@login_required
def recipe_edit_view(request: HttpRequest, pk: int):
    recipe = get_object_or_404(Recipe, pk=pk)

    if recipe.author != request.user:
        return redirect('common:home')

    return _handle_recipe_form_with_formsets(
        request=request,
        form_class=RecipeEditForm,
        template_name='recipes/edit-recipe-page.html',
        recipe=recipe,
    )


class RecipeDeleteView(DeleteView):
    model = Recipe
    form_class = RecipeDeleteForm
    template_name = 'recipes/delete-recipe-page.html'
    success_url = reverse_lazy('common:home')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return super().form_valid(form)
