from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=200)

    def _str_(self):
        return f'{self.name} by {self.description}'
