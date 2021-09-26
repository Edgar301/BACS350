from week5.Superhero.hero.models import Hero
from django.test import TestCase
from .models import Hero


class HeroTest(TestCase):

    def test_django(self):
        self.assertTrue

    def test_num_Hero(self):
        self.assertEqual(len(Hero.objects.all()), 0)

    def test_add_hero(self):
        Hero.objects
        self.assertEqual(len(Hero.objects.all()), 1)
