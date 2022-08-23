from rest_framework import serializers
from .models import Category, RecipeImage, Recipe

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    created_at=serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', read_only=True)
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'text', 'author', 'category','created_at')
    def to_representation(self, instance):
        representation=super().to_representation(instance)
        representation['images'] = RecipeImageSerializer(instance.images.all(), many=True, context=self.context).data
        return representation

class RecipeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeImage
        fields = '__all__'



