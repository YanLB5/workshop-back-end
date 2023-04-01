from rest_framework import viewsets
from .serializers import LivrosSerializer, Compradores_dos_LivrosSerializer, Fornecedor_LivrosSerializer
from .models import Livros, Compradores_dos_Livros, Fornecedor_Livros

class LivrosViewSet(viewsets.ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = Livros

class Compradores_dos_LivrosViewSet(viewsets.ModelViewSet):
    queryset = Compradores_dos_Livros.objects.all()
    serializer_class = Compradores_dos_LivrosSerializer

class Fornecedor_LivrosViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor_Livros.objects.all()
    serializer_class = Fornecedor_LivrosSerializer
