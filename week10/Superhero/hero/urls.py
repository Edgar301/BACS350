
from django.views.generic import RedirectView
from django.urls.conf import include, include
from django.contrib import admin
from django.urls import path

from .views_author import AuthorDeleteView, AuthorDetailView, AuthorListView, AuthorCreateView, AuthorUpdateView
from .views_hero import HeroView, HeroDeleteView, HeroDetailView, HeroListView, HeroCreateView, HeroUpdateView
from .views_chapter import ChapterDeleteView, ChapterDetailView, ChapterListView, ChapterCreateView, ChapterUpdateView


urlpatterns = [

    path('',                            HeroView.as_view(),        name='home'),

    # Author
    path('author/',                     AuthorListView.as_view(),
         name='author_list'),
    path('author/<int:pk>',
         AuthorDetailView.as_view(),  name='author_detail'),
    path('author/add',
         AuthorCreateView.as_view(),  name='author_add'),
    path('author/<int:pk>/',
         AuthorUpdateView.as_view(),  name='author_edit'),
    path('author/<int:pk>/delete',
         AuthorDeleteView.as_view(),  name='author_delete'),

    # Book
    path('hero/',                       HeroListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>',
         HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/add',                    HeroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/',              HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete',
         HeroDeleteView.as_view(),  name='hero_delete'),

    # Chapter
    path('chapter/',                    ChapterListView.as_view(),
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
