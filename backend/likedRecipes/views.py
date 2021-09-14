from .models import LikedRecipe
from .serializers import LikedRecipeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import Http404

# Create your views here.

class LikedRecipeList(APIView):
    
    def get(self, request):
        likedRecipe = LikedRecipe.objects.all()
        serializer = LikedRecipeSerializer(likedRecipe, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = LikedRecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LikedRecipeDetail(APIView):
    
    def get_object(self, pk):
        try:
            return LikedRecipe.objects.get(pk=pk)
        except LikedRecipe.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        likedRecipe = self.get_object(pk)
        serializer = LikedRecipeSerializer(likedRecipe)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        likedRecipe = self.get_object(pk)
        likedRecipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    
        