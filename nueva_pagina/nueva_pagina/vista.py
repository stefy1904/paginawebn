from django.http import HttpResponse;
from django.template import Template, Context;
from api.models import *
from api.forms import *

def pagina_proyecto(request):
    documento = open("C:/Users/vicen/Desktop/pwy/nueva_pagina/nueva_pagina/html/proyecto.html")
    plt = Template(documento.read())
    documento.close()
    ctx = Context()
    pagina = plt.render(ctx)
    return(HttpResponse(pagina))

def pagina_spawns(request):
    documento = open("C:/Users/vicen/Desktop/pwy/nueva_pagina/nueva_pagina/html/spawns.html")
    plt = Template(documento.read())
    documento.close()
    ctx = Context()
    pagina = plt.render(ctx)
    return(HttpResponse(pagina))

def pagina_foro(request):
    documento = open("C:/Users/vicen/Desktop/pwy/nueva_pagina/nueva_pagina/html/foro.html")
    plt = Template(documento.read())
    documento.close()
    ctx = Context()
    pagina = plt.render(ctx)
    return(HttpResponse(pagina))

def pagina_herramientas(request):
    documento = open("C:/Users/vicen/Desktop/pwy/nueva_pagina/nueva_pagina/html/herramientas.html")
    plt = Template(documento.read())
    documento.close()
    ctx = Context()
    pagina = plt.render(ctx)
    return(HttpResponse(pagina))

def pagina_rangos(request):
    documento = open("C:/Users/vicen/Desktop/pwy/nueva_pagina/nueva_pagina/html/rangos.html")
    plt = Template(documento.read())
    documento.close()
    ctx = Context()
    pagina = plt.render(ctx)
    return(HttpResponse(pagina))

def pagina_Formulario(request):
    documento = open("C:/Users/vicen/Desktop/pwy/nueva_pagina/nueva_pagina/html/Formulario.html")
    plt = Template(documento.read())
    documento.close()
    ctx = Context()
    pagina = plt.render(ctx)
    return(HttpResponse(pagina))

def pagina_listar(request):
    documento = open("C:/Users/vicen/Desktop/pwy/nueva_pagina/nueva_pagina/html/listar_usuario.html")
    plt = Template(documento.read())
    documento.close()
    ctx = Context()
    pagina = plt.render(ctx)
    return(HttpResponse(pagina))
