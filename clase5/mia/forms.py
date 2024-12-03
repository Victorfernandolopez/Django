from django import forms

class FormularioCurso(forms.Form):
    profesor = forms.CharField(max_length=50)
    nombre = forms.CharField(label="Nombre del Curso", max_length=50)
    curso = forms.IntegerField()
    inscriptos = forms.IntegerField()
