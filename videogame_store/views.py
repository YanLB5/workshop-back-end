from rest_framework import viewsets
from .serializer import JogoSerializer, LojaSerializer
from .models import Jogo, Loja


class JogoViewset(viewsets.ModelViewSet):
   queryset = Jogo.objects.all()
   serializer_class = JogoSerializer

class LojaViewset(viewsets.ModelViewSet):
   queryset = Loja.objects.all()
   serializer_class = LojaSerializer 