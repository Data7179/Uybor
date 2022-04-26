from django.shortcuts import render
from django.http import JsonResponse
from .models import Uylar, User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UylarSerializer
from rest_framework.permissions import IsAuthenticated


class Uy_Get(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_news = Uylar.objects.all()

        serialized_news = UylarSerializer(data=all_news, many=True)
        serialized_news.is_valid()

        return Response(serialized_news.data)


class Uy_Post(APIView):
    def post(self, request):
            
        serialized_news = UylarSerializer(data=request.data)
        
        if request.user.is_authenticated:
            if serialized_news.is_valid():
                serialized_news.save()
                return Response({"detail": "Yanglik muvaffaqiyatli qo'shildi"})

            return Response({"detail": serialized_news.errors})
