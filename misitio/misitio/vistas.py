from django.http import HttpResponse
from django.template import Template, Context

def pagina_principal(request):

    documento = open("C:/Users/stefa/OneDrive/Escritorio/pwy/misitio/misitio/html/index.html")
    plt = Template(documento.read())
    documento.close()
    ctx = Context()
    pagina = plt.render(ctx)
    return(HttpResponse(pagina))
