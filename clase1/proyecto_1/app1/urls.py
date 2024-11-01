from django.urls import path # para crear rutas
from . import views # para importar las vistas

urlpatterns = [ # lista de rutas
    path('', views.index, name='index'), # ruta por defecto si el usuario no especifica una ruta
]