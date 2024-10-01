# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def sobre(request):
    context = {
        'titulo': 'Fazenda Rei do Gado: Onde a tradição encontra a inovação.',
        'subtitulo': 'Uma história de paixão, dedicação e sustentabilidade no campo.',
        'historia': """
        Nossa história começa com um sonho: cultivar a terra e criar um futuro mais verde. Com dedicação e muito trabalho, transformamos uma pequena propriedade em uma fazenda próspera e sustentável.

        Enfrentamos desafios, mas a paixão pela agricultura nos impulsionou a superar obstáculos e construir um negócio sólido e duradouro. Através de investimentos em tecnologia e práticas sustentáveis, conseguimos otimizar a produção e garantir a qualidade dos nossos produtos.

        Nosso compromisso com a qualidade e o bem-estar animal nos diferencia no mercado. Acreditamos que a natureza é nossa maior aliada e que devemos preservá-la para as futuras gerações.
        """,
        'valores': """
        Sustentabilidade, qualidade, bem-estar animal e transparência
        """,
        'produtos': """
        Produtos frescos e saudáveis e carne bovina de alta qualidade
        """
    }
    return render(request,'sobre.html', context)

def contato(request):
    return render(request, 'contato.html')

def page_perfil_usuario(request, username):
    return HttpResponse(f"Olá {username}, seja bem-vinda ao site Fazenda Rei do Gado.")

def page_home(request):
    return HttpResponse("Fazenda Rei do Gado: Onde a tradição encontra a inovação.")
