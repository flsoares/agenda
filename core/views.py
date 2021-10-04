from django.shortcuts import render,HttpResponse, redirect

# Create your views here.
from core.models import Evento


# def ConsultaEvento(titulo_evento):
#
#     Consulta = Evento.objects.get(Evento.titulo == titulo_evento)
#     return HttpResponse(Consulta.descricao)

# redirecionando quando não for fornecida uma url. ex: http://127.0.0.1:8000/
# Para não trazer page not found
#def index(request):
#    return redirect('/agenda/') # Temos que importar o modulo redirect.


def lista_eventos(request):
    #evento = Evento.objects.get(id = 1)
    #evento = Evento.objects.all # pega todos os eventos.

    #usuario = request.user # Captura o usuario que está enviando a requisição
    #evento = Evento.objects.filter(usuario = usuario)
    # Faz um filtro por usuario da atual sessão
    evento = Evento.objects.all
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)