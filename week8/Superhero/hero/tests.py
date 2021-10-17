from hero.models import Hero
from django.test import TestCase
from django.urls import reverse

from .models import Hero


class HeroCRUDTest(TestCase):

    def test_django(self):
        self.assertTrue

    def test_num_hero(self):
        self.assertEqual(len(Hero.objects.all()), 0)

    def test_add_hero(self):
        Hero.objects.create(name='Thor', description='God OF Thunder')
        Hero.objects.create(name='Ghost', description='Hunter')
        self.assertEqual(len(Hero.objects.all()), 2)

    def test_hero_name(self):
        Hero.objects.create(name='Iliad', dedescription='Homer')
        b = Hero.objects.get(pk=1)
        self.assertEqual(b.name, 'Iliad')
        self.assertEqual(b.description, 'Homer')

    def test_hero_edit(self):
        Hero.objects.create(name='Loki', description='Deception')
        b = Hero.objects.get(pk=1)
        b.name = 'Loki'
        b.save()
        self.assertEqual(b.name, 'Loki')
        self.assertEqual(b.description, 'Deception')

    def test_book_edit(self):
        Hero.objects.create(name='Loki', description='Deception')
        b = Hero.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Hero.objects.all()), 0)

    def test_string_representation(self):
        hero = Hero.objects.create(name='Loki', description='Deception')
        self.assertEqual(
            str(hero), '1 - Loki is Deception')

    class HeroViewsTest(TestCase):

        def test_home(self):
            response = self.client.get('/')
            self.assertEqual(response.status_code, 302)

        def test_get_absolute_url(self):
            hero = Hero.objects.create(
                name='Thor', description='God of Thunder')
            self.assertEqual(hero.get_absolute_url(), '/hero/1')

        def test_hero_list_view(self):
            response = self.client.get(reverse('hero_list'))
            self.assertEqual(response.status_code, 200)

        def test_hero_list_view(self):
            response = self.client.get('/hero/')
            self.assertTemplateUsed(response, 'hero_list.html')
            self.assertTemplateUsed(response, 'superhero_theme.html')
