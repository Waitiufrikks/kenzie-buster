# Generated by Django 4.2.2 on 2023-06-15 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_movieorder_movie_buyers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='buyers',
            new_name='buyed_by',
        ),
    ]
