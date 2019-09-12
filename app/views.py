from django.shortcuts import render
from . import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

class TravelListView(ListView):
    model = models.Travel
    template_name= 'vcard/index-horizontal-portfolio.html'
    fields = '__all__'

    def get_queryset(self):
        return models.Travel.objects.order_by('date', 'hour')

class TravelNewView(CreateView):
    model = models.Travel
    template_name = 'vcard/addviagem.html'
    success_url = reverse_lazy('travel-create')
    fields = '__all__'

class TravelUpdateView(UpdateView):
    model = models.Travel
    templete_name = 'vcard/addviagem.html'
    success_url = reverse_lazy('travel-list')
    fields = '__all__'

class TemplateService(TemplateView):
    template_name = 'vcard/index-horizontal-services.html'
    fields = '__all__'

class TemplateInicial(TemplateView):
    template_name = 'vcard/index-horizontal-about.html'

class UserNewView(CreateView):
    model = User
    template_name = 'vcard/index-horizontal-contact.html'
    success_url = reverse_lazy('travel-list')
    fields = ('first_name', 'email', 'username')

class TemplateLogin(TemplateView):
    template_name = 'vcard/login.html'
    success_url = reverse_lazy('travel-list')

class TemplateMinhasViagens(TemplateView):
    template_name = 'vcard/Minhasviagens.html'
    success_url = reverse_lazy('minhasviagens')

class TemplateViagensamigos(TemplateView):
    template_name = 'vcard/ViagensDosMeusAmigos.html'
    success_url = reverse_lazy('viagensamigos')


