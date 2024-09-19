"""
URL configuration for Controle_Estoque project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.http import HttpResponse

def page_home(request):
    return HttpResponse("Fazenda Rei do Gado: Onde a tradição encontra a inovação.")

def page_sobre(request):
    return HttpResponse("Este site é sobre uma Fazenda onde há criações de gado de corte e de leite./n Nosso intuito é levar a vocês nosso produtos de ótima qualidade!!!")

def page_perfil_usuario(request, username):
    return HttpResponse(f"Olá {username}, seja bem-vinda ao site Fazenda Rei do Gado.")

def page_contato(request):
    return HttpResponse("""
        Entre em contato conosco para saber mais do nosso trabalho :)<br>
        Tel: (35) 9 9999-9999<br>
        E-mail: contato@fazendarg.com.br<br>
        Caso queira fazer-nos uma visita, você nos encontrará no endereço:<br>
        <strong>Fazenda Rei do Gado</strong><br>
        Estrada Municipal, Km 25, Zona Rural<br>
        CEP: 12345-678<br>
        Município de Itajubá, MG
    """)

urlpatterns = [
    path('', page_home),
    path('sobre/', include('sobre_fazenda.urls')),
    path('user/<str:username>', page_perfil_usuario),
    path('contato/', page_contato)
]