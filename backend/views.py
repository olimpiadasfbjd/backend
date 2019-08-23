from django.shortcuts import render
from backend.models import Data
from backend.serializers import DataSerializer
from rest_framework import viewsets


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
