# Generated by Django 4.2.7 on 2023-11-26 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0012_alter_genre_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]