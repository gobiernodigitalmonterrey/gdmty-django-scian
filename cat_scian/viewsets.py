
# Viewsets for SCIAN

from rest_framework import viewsets
from .models import SCIAN
from .serializers import SCIANSerializer

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class ScianViewSet(viewsets.ModelViewSet):
    queryset = SCIAN.objects.all()
    serializer_class = SCIANSerializer
    filterset_fields = ['id', 'nivel']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['titulo', 'descripcion', 'incluye', 'excluye', 'indice']