from django.views.generic import RedirectView
from django.urls.conf import include, include
from django.contrib import admin
from django.urls import path

from hero.views import HeroView, HeroDeleteView, HeroDetailView, HeroListView, HeroCreateView, HeroUpdateView

urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),

    # Hero Views
    path('', HeroView.as_view()),
    path('hero/',                   HeroListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>',           HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/add',                HeroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/',          HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete',    HeroDeleteView.as_view(),  name='hero_delete'),

]
