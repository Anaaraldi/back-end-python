from django.urls import path
from fazenda.views import sobre, contato, page_perfil_usuario, page_home

urlpatterns = [
    path('',page_home ),
    path('contato/', contato,),
    path('sobre/',sobre),
    path('user/<str:username>', page_perfil_usuario),
 ]