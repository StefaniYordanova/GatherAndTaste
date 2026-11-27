from django.db import models


class Tag(models.TextChoices):
    VEGAN = 'Vegan', 'Vegan'
    VEGETARIAN = 'Vegetarian', 'Vegetarian'
    GLUTEN_FREE = 'Gluten-Free', 'Gluten-Free'
    HEALTHY = 'Healthy', 'Healthy'
    PROTEIN = 'Protein', 'Rich in protein'
    FIBER = 'Fiber', 'Rich in fibers'
    SUGAR_FREE = 'Sugar Free', 'Sugar Free'


class Difficulty(models.TextChoices):
    EASY = 'Easy', 'Easy'
    MEDIUM = 'Medium', 'Medium'
    HARD = 'Hard', 'Hard'


class Visibility(models.TextChoices):
    PUBLIC = 'Public', 'Public'
    PRIVATE = 'Private', 'Private'


class IngredientUnit(models.TextChoices):
    GRAM = "g", "g"
    KILOGRAM = "kg", "kg"
    LITER = "l", "l"
    TEASPOON = "tsp", "tsp"
    TABLESPOON = "tbsp", "tbsp"
    PIECE = "pcs", "pcs"
    CLOVE = "clove", "clove"
    SLICE = "slice", "slice"
    CUPS = "cup", "cup"
