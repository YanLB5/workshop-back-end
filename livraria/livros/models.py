from django.db import models

class Livros(models.Model):
    título = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano_de_lançamento = models.CharField(max_length=100)
    
    def __str__(self):
        return self.título
    
       
class Compradores_dos_Livros(models.Model):
    CPF = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    endereço = models.CharField(max_length=100)

    def __str__(self):
        return self.CPF
    
class Fornecedor_Livros(models.Model):
    CNPJ = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    endereço = models.CharField(max_length=100)

    def __str__(self):
        return self.CNPJ
