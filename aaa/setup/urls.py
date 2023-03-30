from django.contrib import admin
from django.urls import path, include
from videogame_store.views import JogoViewset, LojaViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('jogos', JogoViewset, basename = 'Jogos')
router.register('lojas', LojaViewset, basename = 'Loja')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
    
]
