from django.shortcuts import render
from django.http import HttpResponse # para devolver una respuesta

# Create your views here.


def index(request):# funcion que se llama por la url
    return HttpResponse("Hola Mundo")# devolver una respuesta
