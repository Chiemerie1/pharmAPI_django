from django.http import JsonResponse, HttpResponse

from rest_framework.parsers import JSONParser

from .models import Types, Drugs 
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, viewsets
from .serializers import UserSerializer, GroupSerializer,TypesSerializers, DrugSerializers


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


@csrf_exempt
def drugs_list(request):
    
    if request.method == "GET":
        drugs = Drugs.objects.all()
        serializer = DrugSerializers(drugs, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method =="POST":
        data = JSONParser().parse(request)
        serializer = DrugSerializers(data=data)
        if serializer.is_valid():
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def drugs_info(request, pk):
    try:
        drug = Drugs.objects.get(pk=pk)
    except Drugs.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = DrugSerializers(drug)
        return JsonResponse(serializer.data)
    
    elif request.method =="PUT":
        data = JSONParser().parse(request)
        serializer = DrugSerializers(drug, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.errors, status=400)
    
    elif request.method == "DELETE":
        drug.delete()
        return HttpResponse(status=204)


def type_list(request):
    if request.method == "GET":
        types = Types.objects.all()
        type_serializer = TypesSerializers(types, many=True)
        return JsonResponse(type_serializer.data, safe=False)
    elif request.method =="POST":
        data = JSONParser().parse(request)
        type_serializer = TypesSerializers(data=data)
        if type_serializer.is_valid():
            return JsonResponse(type_serializer.data, status=201)
        return JsonResponse(type_serializer.errors, status=400)


@csrf_exempt
def types_info(request, pk):
    try:
        type = Types.objects.get(pk=pk)
    except Types.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        types_serializer = TypesSerializers(type)
        return JsonResponse(types_serializer.data)
    
    elif request.method =="PUT":
        data = JSONParser().parse(request)
        types_serializer = TypesSerializers(type, data=data)
        if types_serializer.is_valid():
            types_serializer.save()
            return JsonResponse(types_serializer.errors, status=400)
    
    elif request.method == "DELETE":
        type.delete()
        return HttpResponse(status=204)




# class StringView(APIView):
#     def get(self, request, *args, **kwargs):
#         info = {"drug": "drug name", "status": "available"}
#         return Response(info)