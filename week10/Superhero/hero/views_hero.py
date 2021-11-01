from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView
from django.views.generic.base import TemplateView

from .models import Hero, Chapter


class HeroView(RedirectView):
    url = '/hero/'


class HeroListView(ListView):
    template_name = 'hero_list.html'
    model = Hero


class HeroDetailView(DetailView):
    template_name = 'hero_detail.html'
    model = Hero

    def get_context_data(self, **kwargs):
        hero = Hero.objects.get(pk=self.kwargs['pk'])
        return dict(object=hero, chapters=Chapter.objects.filter(hero=hero.name))


class HeroCreateView(LoginRequiredMixin, CreateView):
    template_name = "hero_add.html"
    model = Hero
    fields = ['title', 'author', 'description', 'doc_path']


class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "hero_edit.html"
    model = Hero
    fields = ['title', 'author', 'description', 'doc_path']


class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Hero
    template_name = 'hero_delete.html'
    success_url = reverse_lazy('hero_list')
