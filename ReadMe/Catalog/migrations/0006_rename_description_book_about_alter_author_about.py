# Generated by Django 4.2.7 on 2023-11-19 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0005_author_image_alter_book_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='description',
            new_name='about',
        ),
        migrations.AlterField(
            model_name='author',
            name='about',
            field=models.TextField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
