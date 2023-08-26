from rest_framework import serializers
from .models import AssetHolder, Animal, AnimalGrade, ValuePoint, AnimalResource


class AssetHolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetHolder
        fields = "__all__"


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"


class AnimalGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalGrade
        fields = "__all__"


class ValuePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValuePoint
        fields = "__all__"


class AnimalResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalResource
        fields = "__all__"
