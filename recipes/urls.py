from django.urls import path, include
from . import views

app_name = 'recipes'

urlpatterns = [
    path('add/', views.recipe_create_view, name='add'),
    path('<int:pk>/', include([
        path('edit/', views.recipe_edit_view, name='edit'),
        path('delete/', views.RecipeDeleteView.as_view(), name='delete'),
    ])),

]