
from django.views.generic import RedirectView
from django.urls.conf import include, include
from django.contrib import admin
from django.urls import path

from .views_hero import BookView, BookDeleteView, BookDetailView, BookListView, BookCreateView, BookUpdateView
from .views_chapter import ChapterDeleteView, ChapterDetailView, ChapterListView, ChapterCreateView, ChapterUpdateView


urlpatterns = [

    # Book
    path('',                        BookView.as_view(),        name='home'),
    path('hero/',                   BookListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>',           BookDetailView.as_view(),  name='hero_detail'),
    path('hero/add',                BookCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/',          BookUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete',    BookDeleteView.as_view(),  name='hero_delete'),

    # Chapter
    path('chapter/',                   ChapterListView.as_view(),
         name='chapter_list'),
    path('chapter/<int:pk>',
         ChapterDetailView.as_view(),  name='chapter_detail'),
    path('chapter/add',
         ChapterCreateView.as_view(),  name='chapter_add'),
    path('chapter/<int:pk>/',
         ChapterUpdateView.as_view(),  name='chapter_edit'),
    path('chapter/<int:pk>/delete',
         ChapterDeleteView.as_view(),  name='chapter_delete'),

]
