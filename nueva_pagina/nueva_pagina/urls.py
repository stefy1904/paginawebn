
from django.contrib import admin
from django.urls import path
from nueva_pagina.vista import *
from api.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pagina_proyecto/',pagina_proyecto),
    path('pagina_spawns/',pagina_spawns),
    path('pagina_foro/',pagina_foro),
    path('pagina_rangos/',pagina_rangos),
    path('pagina_herramientas/',pagina_herramientas),
    path('pagina_Formulario/',foro),
    path('listar_usuario/',listar_usuario),




]
