from django.contrib import admin
from main.models import Recipe, Category, RecipeImage

class RecipeImageInLine(admin.TabularInline):
    model = RecipeImage
    max_num = 10
    min_num = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeImageInLine,]

admin.site.register(Category)
# admin.site.register(Recipe)
# admin.site.register(RecipeImage)


