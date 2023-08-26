from rest_framework import generics
from .models import AssetHolder, Animal, AnimalGrade, ValuePoint, AnimalResource
from .serializers import (
    AssetHolderSerializer,
    AnimalSerializer,
    AnimalGradeSerializer,
    ValuePointSerializer,
    AnimalResourceSerializer,
)


class AssetHolderList(generics.ListCreateAPIView):
    queryset = AssetHolder.objects.all()
    serializer_class = AssetHolderSerializer


class AnimalList(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalGradeList(generics.ListCreateAPIView):
    queryset = AnimalGrade.objects.all()
    serializer_class = AnimalGradeSerializer


class ValuePointList(generics.ListCreateAPIView):
    queryset = ValuePoint.objects.all()
    serializer_class = ValuePointSerializer


class AnimalResourceList(generics.ListCreateAPIView):
    queryset = AnimalResource.objects.all()
    serializer_class = AnimalResourceSerializer
