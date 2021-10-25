from django.db import models
from django.urls.base import reverse_lazy


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
# document - path to markdown file


class Chapter(models.Model):
    book = models.CharField(max_length=200, default="Leverage Principle")
    # book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=200)
    markdown = models.TextField()
    html = models.TextField()
    document = models.CharField(max_length=200)

    def export_record(self):
        return [self.book, self.order, self.title]

    @staticmethod
    def import_record(values):
        c = Chapter.objects.get_or_create(book=values[0], order=values[1])[0]
        c.title = values[2]
        c.save()

    def __str__(self):
        return f'{self.book.title} - {self.order} - {self.title}'
