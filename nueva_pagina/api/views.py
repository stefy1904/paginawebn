from django.shortcuts import render
from .models import Usuario
from .forms import UsuarioForm
# Create your views here.
def inicio (request):
    return render(request, 'proyecto.html')

def foro (request):
    data={
    'form':UsuarioForm(),
    }
    if request.method == 'POST':
        foro = UsuarioForm(request.POST)
        if foro.is_valid():
            foro.save()
            data['mensaje'] = "guardado!!"

        else:
            data['mensajeE'] = "hubo un error al enviar"


    return render(request, 'Formulario.html',data)

def listar_usuario (request):
    Personas = Usuario.objects.all()
    data = {
        'user': Personas,

    }
    return render(request,'listar_usuario.html',data)
