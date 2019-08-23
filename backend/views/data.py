from rest_framework import filters, viewsets

from backend.models import Data
from backend.serializers import DataSerializer


class DataViewSet(viewsets.ModelViewSet):

    queryset = Data.objects.all()
    serializer_class = DataSerializer