from django.db import models
from django.urls.base import reverse_lazy
from django.contrib.auth.models import User


# --------------------
# Author
#
# user - login credentials for author
# name - name of author

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.pk} - {self.name}'


# --------------------
# Book
#
# title - title of the book
# author - name of author
# description - summary of the book

class Hero(models.Model):
    name = models.CharField(max_length=100)
    identity = models.CharField(default='None', max_length=100)
    description = models.TextField()
    strength = models.CharField(default='None', max_length=100)
    weakness = models.CharField(default='None', max_length=100)
    image = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.pk} - {self.name} by {self.description}'

    def get_absolute_url(self):
        return reverse_lazy('hero_detail', args=[str(self.id)])


# --------------------
# Chapter
#
# book - points to book object
# order - chapter order
# title - title text of chapter
# markdown - markdown text
# html - HTML text from markdown
# document - path to markdown file

class Chapter(models.Model):
    hero = models.CharField(max_length=200, default="Leverage Principle")
    # book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=200)
    markdown = models.TextField()
    html = models.TextField()
    document = models.CharField(max_length=200)

    def export_record(self):
        return [self.order, self.title, self.document]

    @staticmethod
    def import_record(hero, values):
        c = Chapter.objects.get_or_create(hero=hero.title, order=values[0])[0]
        c.title = values[1]
        c.document = values[2]
        c.save()

    def __str__(self):
        return f'{self.hero.title} - {self.order} - {self.title}'

    def get_absolute_url(self):
        return reverse_lazy('chapter_detail', args=[str(self.id)])
