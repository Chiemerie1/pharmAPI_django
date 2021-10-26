from rest_framework import serializers
from .models import Types, Drugs, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User, Group



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class TypesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = [
            "name",
            "desc",
        ]

class DrugSerializers(serializers.ModelSerializer):
    class Meta:
        model = Drugs
        fields = [
            "types", "name",
            "indications",
            "contraindications",
            "price",  "status"
        ]
        