from django.shortcuts import render
from django.http import HttpResponse
from .models import Tecnologias

def nova_empresa(request):
    if request.method == "GET":
        techs = Tecnologias.objects.all()    
        return render(request, 'nova_empresa.html', {'techs':techs})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cidade = request.POST.get('cidade')
        endereco = request.POST.get('endereco')
        nicho = request.POST.get('nicho')
        caracteriscas = request.POST.get('caracteristicas')
        
        return HttpResponse("Tô aqui")