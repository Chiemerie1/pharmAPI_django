from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response



class StringView(APIView):
    def get(self, request, *args, **kwargs):
        info = {"drug": "drug name", "status": "available"}
        return Response(info)