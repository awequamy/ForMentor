from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import Category, Recipe
from .serializers import CategorySerializer, RecipeSerializer

import json


@api_view(['GET'])
def categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

class RecipeListView(APIView):
    def get(self,request):
        recipes=Recipe.objects.all()
        serializer=RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request):
        recipe = request.data
        serializer = RecipeSerializer(data=recipe)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response('')










