import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from . import forms
from django.urls import reverse
from .models import Curso,Adidas

def index (request):
    return HttpResponse("Hello, world. You're at the polls index.")