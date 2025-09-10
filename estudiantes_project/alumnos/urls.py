from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('registro/', views.registrar_alumno, name='registro_alumno'),
]