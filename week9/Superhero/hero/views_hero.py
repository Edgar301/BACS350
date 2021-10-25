from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView
from django.views.generic.base import TemplateView

from .models import Hero, Chapter


class BookView(RedirectView):
    url = '/hero/'


class BookListView(ListView):
    template_name = 'hero_list.html'
    model = Hero


class BookDetailView(DetailView):
    template_name = 'hero_detail.html'
    model = Hero

    def get_context_data(self, **kwargs):
        book = Hero.objects.get(pk=self.kwargs['pk'])
        return dict(object=book, chapters=Chapter.objects.filter(hero=book.title))


class BookCreateView(LoginRequiredMixin, CreateView):
    template_name = "hero_add.html"
    model = Hero
    fields = ['name', 'description']


class BookUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "hero_edit.html"
    model = Hero
    fields = ['name', 'description']


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Hero
    template_name = 'hero_delete.html'
    success_url = reverse_lazy('book_list')
