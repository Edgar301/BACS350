# Generated by Django 3.2.6 on 2021-10-25 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0003_chapter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name="book",
            new_name='hero',
        ),
    ]
