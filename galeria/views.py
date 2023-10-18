from django.shortcuts import render

def index(req):
    return render(req, 'Galeria/index.html');

def imagem(req):
    return render(req, 'Galeria/imagem.html')