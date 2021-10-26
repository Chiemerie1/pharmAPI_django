from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import Types, Drugs 
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer,TypesSerializers, DrugSerializers

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import permissions, viewsets
from rest_framework import status


# Create your views here.

# from rest_framework.views import APIView
# from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



@api_view(["GET", "POST"])
def drugs_list(request, format=None):
    
    if request.method == "GET":
        drugs = Drugs.objects.all()
        serializer = DrugSerializers(drugs, many=True)
        return Response(serializer.data)
    elif request.method =="POST":
        serializer = DrugSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET", "PUT", "DELETE"])
def drugs_info(request, pk, format=None):
    try:
        drug = Drugs.objects.get(pk=pk)
    except Drugs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = DrugSerializers(drug)
        return Response(serializer.data)
    
    elif request.method =="PUT":
        serializer = DrugSerializers(drug, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        drug.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def type_list(request, format=None):
    if request.method == "GET":
        types = Types.objects.all()
        type_serializer = TypesSerializers(types, many=True)
        return Response(type_serializer.data)
    elif request.method =="POST":
        type_serializer = TypesSerializers(data=request.data)
        if type_serializer.is_valid():
            return Response(type_serializer.data, status=status.HTTP_201_CREATED)
        return Response(type_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET", "PUT", "DELETE"])
def types_info(request, pk, format=None):
    try:
        type = Types.objects.get(pk=pk)
    except Types.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        types_serializer = TypesSerializers(type)
        return Response(types_serializer.data)
    
    elif request.method =="PUT":
        types_serializer = TypesSerializers(type, data=request.data)
        if types_serializer.is_valid():
            types_serializer.save()
            return Response(types_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# class StringView(APIView):
#     def get(self, request, *args, **kwargs):
#         info = {"drug": "drug name", "status": "available"}
#         return Response(info)