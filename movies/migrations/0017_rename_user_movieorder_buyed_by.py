# Generated by Django 4.2.2 on 2023-06-16 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0016_rename_buyers_movie_buyed_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movieorder',
            old_name='user',
            new_name='buyed_by',
        ),
    ]
