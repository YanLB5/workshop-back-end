from django.contrib import admin
from django.urls import path, include
from livros.viewsets import LivrosViewSet, Compradores_dos_LivrosViewSet, Fornecedor_LivrosViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('livros', LivrosViewSet, basename='livros')
router.register('compradores dos livros', Compradores_dos_LivrosViewSet, basename='Compradores_dos_Livros')
router.register('fornecedor dos livros', Fornecedor_LivrosViewSet, basename='fornecedor_livros')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
