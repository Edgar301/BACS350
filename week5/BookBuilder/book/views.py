from django.views.generic import ListView, TemplateView
from .models import Book


class IndexView(TemplateView):
    template_name = 'index.html'
