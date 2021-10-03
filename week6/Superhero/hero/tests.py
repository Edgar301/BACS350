
from django.test import TestCase
from .models import Hero


class HeroTest(TestCase):

    def test_django(self):
        self.assertTrue

    def test_num_Hero(self):
        self.assertEqual(len(Hero.objects.all()), 0)

    def test_add_hero(self):
        Hero.objects.create(title='Strongest Avenger', name='Thor')
        Hero.objects.create(title='God of Deception', name='Loki')

        self.assertEqual(len(Hero.objects.all()), 1)
