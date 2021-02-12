from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def candidato(request):
    return render(request, 'candidato.html')


def empresa(request):
    return render(request, 'empresa.html')


def sobre(request):
    return render(request, 'sobre.html')
