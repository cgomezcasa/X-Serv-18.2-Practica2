from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from .models import Urls
from sqlite3 import OperationalError
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

formulario = """
        <form action="" method="POST">
          <h3>URL:</h3>
          <input type="text" name="URL" value="http://"><br>
          <input type="submit" value="Enviar">
        </form>
        """

def nameUrl(url):
    if url.startswith('http://') or url.startswith('https://'):
        return url
    else:
        return('http://' + url)

@csrf_exempt
def barra(request):
    if request.method == 'GET':
        list = Urls.objects.all()
        resp = "<h3>LISTA: </h3><ul>"

        try:
            for objeto in list:
                resp += '<li><a href="' + str(objeto.id) + '">' + objeto.name + '</a>'
            resp += "</ul>"
        except OperationalError:
            resp = "No hay nada en la lista."

        return HttpResponse(formulario + resp)
        
    elif request.method == 'POST':
        url = Urls(name=nameUrl(request.POST['URL']))
        try:
            url.save()
            return HttpResponse(url)
        except IntegrityError:
            return HttpResponse("Página ya añadida en la lista anteriormente.")
        


def getUrl(request, recurso):
    if request.method == 'GET':
        try:
            objeto = Urls.objects.get(id = int(recurso))
            return HttpResponseRedirect(objeto.name)
        except Urls.DoesNotExist:
            return HttpResponse("No encontrado", status=404)
        

def notOption(request, recurso):
    return HttpResponse("No contemplada esta opción.", status=404)

