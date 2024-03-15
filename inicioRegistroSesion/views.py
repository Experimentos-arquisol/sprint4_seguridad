from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def registro(request):

    if request.method == 'GET':
        return render(request, 'cliente/registro')


