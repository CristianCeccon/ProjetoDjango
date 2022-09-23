from dataclasses import fields
from re import template
import django
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Campo, Robos

from django.urls import reverse_lazy

# Create your views here.
class CampoCreaete(CreateView):
    model= Campo
    fields= ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class RobosCreate(CreateView):
    model= Robos
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
####

class CampoUpdate(UpdateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    

class RobosUpdate(UpdateView):
    model = Robos
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

####


class CampoDelete(DeleteView):
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')


class RobosDelete(DeleteView):
    model = Robos
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

####


class CampoList(ListView):
    model = Campo
    template_name = 'cadastros/listas/campo.html'


class RobosList(ListView):
    model = Robos
    template_name = 'cadastros/listas/robos.html'
