import sqlite3
from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.
def home(request):
    return HttpResponse('Bienvenidos a la clase de Django')

def acerca(request):
    return render(request, 'mia/acerca.html')

def expl_form(request):
    return render(request, 'mia/expl_form.html')

def curso(request):
    if request.method == 'POST':
        miForm = forms.FormularioCurso(request.POST)
        if miForm.is_valid():
            nombre = miForm.cleaned_data['nombre']
            profesor = miForm.cleaned_data['profesor']
            inscriptos = miForm.cleaned_data['inscriptos']
            cursos = miForm.cleaned_data['curso']
            conn = sqlite3.connect('clase5.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO cursos (nombre, profesor, inscriptos, cursos) VALUES (?, ?, ?, ?)", (nombre, profesor, inscriptos, cursos))
            conn.commit()
            conn.close()
            return HttpResponse(f"Curso grabado exitosamente: {nombre} !")
    else:
        miForm = forms.FormularioCurso()

    return render(request, 'mia/cursoForm.html', {'form':miForm})
    