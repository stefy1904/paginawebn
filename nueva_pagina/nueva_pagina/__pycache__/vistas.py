from django.http import HttpResponse;


def pagina_inicio(request):
    pagina="""<html>
    <head>
    </head>
    <body>
    <h1 style="color:red">mensaje de la nueva pagina</h1>
    </body>
    </html>"""
    return(HttpResponse(pagina))
