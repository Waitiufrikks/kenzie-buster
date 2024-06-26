# Generated by Django 4.2.2 on 2023-06-14 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0005_alter_movie_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='movies', to=settings.AUTH_USER_MODEL),
        ),
    ]
