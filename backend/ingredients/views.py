from .models import Ingredient
from .serializers import IngredientSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import Http404

# Create your views here.

class IngredientList(APIView):
    
    def get(self, request):
        ingredient = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredient, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class IngredientDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Ingredient.objects.get(pk=pk)
        except Ingredient.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        ingredient = self.get_object(pk)
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)