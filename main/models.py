from django.db import models

from account.models import MyUser


class Category(models.Model):
    slug = models.SlugField(max_length=100,primary_key=True)
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='recipe')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipe')
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class RecipeImage(models.Model):
    image = models.ImageField(upload_to='recipes', blank=True, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='images')










