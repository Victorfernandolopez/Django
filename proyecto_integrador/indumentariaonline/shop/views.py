from django.shortcuts import render

from .models import Remera


def index(request):
    remeras = Remera.objects.all()
    ctx = {"remeras": remeras}
    return render(request, "shop/index.html", ctx)


def contacto(request):
    return render(request, "shop/contacto.html")

