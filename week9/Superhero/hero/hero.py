from os.path import exists

from hero.models import Chapter
from table.table import read_csv_file, write_csv_file


def export_chapters(hero):
    model = Chapter
    chapters = f'{hero.doc_path}/chapters.csv'
    records = [o.export_record()
               for o in model.objects.filter(hero=hero.title)]
    write_csv_file(chapters, records)


def import_chapters(hero):
    model = Chapter
    chapters = f'{hero.doc_path}/chapters.csv'
    if exists(chapters):
        for row in read_csv_file(chapters):
            model.import_record(row)
