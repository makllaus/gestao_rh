from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView

from apps.empresas.models import Empresa


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome',]

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return reverse('home')

class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome',]
