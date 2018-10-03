from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.http import JsonResponse
# Create your views here.

class UsersView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=404)
