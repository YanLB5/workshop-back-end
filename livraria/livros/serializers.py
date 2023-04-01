from rest_framework import serializers
from .models import Livros, Compradores_dos_Livros, Fornecedor_Livros

class LivrosSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Livros
        fields=['título', 'autor', 'ano_de_lançamento']

class Compradores_dos_LivrosSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Compradores_dos_Livros
        fields=['CPF', 'telefone', 'endereço']

class Fornecedor_LivrosSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Fornecedor_Livros
        fields=['CNPJ', 'email', 'endereço']
