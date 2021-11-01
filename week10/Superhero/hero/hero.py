from os.path import exists

from django.contrib.auth import get_user_model

from hero.models import Author, Hero, Chapter
from table.table import read_csv_file, write_csv_file


def create_hero(**kwargs):
    name = kwargs.get('name')
    description = kwargs.get('description')
    hero = Hero.objects.get_or_create(name=name, description=description)[0]
    hero.doc_path = kwargs.get('doc_path')
    hero.weakness = kwargs.get('weakness')
    hero.save()
    return hero


def create_author(name):
    user = get_user_model().objects.get(pk=1)
    return Author.objects.get_or_create(name=name, user=user)[0]


def export_chapters(hero):
    model = Chapter
    chapters = f'{hero.doc_path}/chapters.csv'
    records = [o.export_record()
               for o in model.objects.filter(hero=hero.title)]
    write_csv_file(chapters, records)


def import_chapters(hero):
    model = Chapter
    chapters = f'{hero.doc_path}/chapters.csv'
    # print(chapters)
    assert(exists(chapters))
    if exists(chapters):
        for row in read_csv_file(chapters):
            # print(row)
            model.import_record(hero, row)


def import_leverage_hero():
    author = create_author('Mark Seaman')
    hero = dict(title="The Leverage Principle",
                author=author,
                description="Software Engineering Skills",
                doc_path='Documents/Leverage')
    b = create_hero(**hero)
    import_chapters(b)


def import_poems_hero():
    author = create_author('Mark Seaman')
    hero = dict(title="A Seaman's Poems",
                author=author,
                description="From the Edge of Reality",
                doc_path='Documents/Poems')
    b = create_hero(**hero)
    import_chapters(b)
