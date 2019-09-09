from django.shortcuts import render
from . import models
from django.utils import timezone

# Create your views here.

class TravelListView(ListView):
    model = models.Travel
    template_name= 'travel/list.html'

    def get_queryset(self):
        return models.Travel.object.order_by(date, hour)