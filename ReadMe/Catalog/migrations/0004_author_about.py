# Generated by Django 4.2.7 on 2023-11-17 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0003_book_image_alter_book_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='about',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
