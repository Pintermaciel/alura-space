from django.shortcuts import render, get_object_or_404
from galeria.models import fotografia

def index(request):
    fotografias = fotografia.objects.filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards" : fotografias})

def imagem(request, foto_id):
    foto = get_object_or_404(fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"foto": foto})

def buscar(resquest):
    fotografias = fotografia.objects.filter(publicada=True)

    if 'buscar' in resquest.GET:
        nome_fotografia = resquest.GET['buscar']
        if nome_fotografia:
            fotografias = fotografias.filter(nome__icontains=nome_fotografia)

    return render(resquest, "galeria/buscar.html", {"cards" : fotografias})