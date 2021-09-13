from .models import RecipeIngredient
from .serializers import RecipeIngredientSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import Http404
# Create your views here.

class RecipeIngredientsFunctions(APIView):
    
    def getAll(self, request):
        recipeIngredient = RecipeIngredient.objects.all()
        serializer = RecipeIngredientSerializer(recipeIngredient, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RecipeIngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_object(self, pk):
        try:
            return RecipeIngredient.objects.get(pk=pk)
        except RecipeIngredient.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        recipeIngredient = self.get_object(pk)
        serializer = RecipeIngredientSerializer(recipeIngredient)
        return Response(serializer.data)
    