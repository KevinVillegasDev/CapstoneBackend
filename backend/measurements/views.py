from .models import Measurement
from .serializers import MeasurementSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class MeasurementFunction(APIView):
    
    def get(self, request):
        measurement = Measurement.objects.all()
        serializer = MeasurementSerializer(measurement, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)