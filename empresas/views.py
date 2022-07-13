from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView
from .models import Empresa


# Create your views here.
class EmpresaCreate(CreateView):
    model= Empresa
    fields = ['nome', ]
    
    def form_valid(self, form):
        objeto = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresas = objeto
        funcionario.save()
        return HttpResponse('OK')