from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('acerca/',acerca, name='acerca'),
    path('expl_form/',expl_form, name='expl_form'),
    path('curso/',curso, name='curso'),
]