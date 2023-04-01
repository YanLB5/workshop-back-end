from rest_framework import viewsets
from livros import serializers
from livros import models

class LivrosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LivrosSerializer
    queryset = models.Livros.objects.all()

class Compradores_dos_LivrosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Compradores_dos_LivrosSerializer
    queryset = models.Compradores_dos_Livros.objects.all()

class Fornecedor_LivrosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Fornecedor_LivrosSerializer
    queryset = models.Fornecedor_Livros.objects.all()