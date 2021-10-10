from typing import List
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView

from .models import Hero


class HeroView(RedirectView):
    url = '/hero/'


class HeroListView(ListView):
    template_name = 'hero_list.html'
    model = Hero


class HeroDetailView(DetailView):
    template_name = 'hero_detail.html'
    model = Hero


class HeroCreateView(CreateView):
    template_name = "Hero_add.html"
    model = Hero
    fields = ['name', 'description']


class HeroUpdateView(UpdateView):
    template_name = "hero_edit.html"
    model = Hero
    fields = ['name', 'description']

    # , 'identity', 'strength ', 'weakness'


class HeroDeleteView(DeleteView):
    model = Hero
    template_name = 'hero_delete.html'
    success_url = reverse_lazy('hero_list')
